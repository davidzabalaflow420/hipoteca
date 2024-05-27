from flask import Blueprint, render_template, request
from Modell import HipotecaInversa
import psycopg2

main = Blueprint('main', __name__)

# Conexión a la base de datos
conn = psycopg2.connect("postgresql://BattleShip_owner:0XuBfor6mAEa@ep-gentle-water-a5djsrmk.us-east-2.aws.neon.tech/HipotecaInversaCalculator?sslmode=require")
cur = conn.cursor()

@main.route('/')
def index():
    """
    Renderiza la página de inicio.

    Returns:
    - str: La plantilla HTML para la página de inicio.
    """
    return render_template('index.html')

@main.route('/calcular', methods=['POST'])
def calcular():
    """
    Realiza el cálculo de la hipoteca inversa según los parámetros proporcionados
    por el usuario y guarda los resultados en la base de datos.

    Returns:
    - str: La plantilla HTML para la página de resultados.
    """
    valor_vivienda = float(request.form['valor_vivienda'])
    edad = int(request.form['edad'])
    interes_anual = float(request.form['interes_anual'])
    renta_mensual = float(request.form['renta_mensual'])
    tipo = request.form['tipo']
    años = int(request.form['años']) if 'años' in request.form and request.form['años'] else 0
    esperanza_vida = int(request.form['esperanza_vida']) if 'esperanza_vida' in request.form and request.form['esperanza_vida'] else 0

    hipoteca = HipotecaInversa(valor_vivienda, edad, interes_anual, renta_mensual)

    if tipo == 'temporal':
        resultado = hipoteca.hipoteca_inversa_temporal(años)
    elif tipo == 'vitalicia':
        resultado = hipoteca.hipoteca_inversa_vitalicia(esperanza_vida)
    elif tipo == 'unica':
        resultado, meses = hipoteca.hipoteca_inversa_unica()
        # Guardar resultado en la base de datos
        insert_query = "INSERT INTO resultados (tipo, valor_vivienda, edad, interes_anual, renta_mensual, resultado, meses) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (tipo, valor_vivienda, edad, interes_anual, renta_mensual, resultado, meses)
        cur.execute(insert_query, values)
        conn.commit()
        return render_template('resultado.html', resultado=resultado, meses=meses, tipo=tipo)
    else:
        resultado = None

    # Guardar resultado en la base de datos
    insert_query = "INSERT INTO resultados (tipo, valor_vivienda, edad, interes_anual, renta_mensual, resultado, años, esperanza_vida) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (tipo, valor_vivienda, edad, interes_anual, renta_mensual, resultado, años, esperanza_vida)
    cur.execute(insert_query, values)
    conn.commit()

    return render_template('resultado.html', resultado=resultado, tipo=tipo)

# Cerrar la conexión a la base de datos al finalizar
@main.route('/shutdown')
def shutdown():
    """
    Cierra la conexión a la base de datos.

    Returns:
    - str: Un mensaje indicando que la conexión ha sido cerrada.
    """
    conn.close()
    return 'Conexión cerrada'
