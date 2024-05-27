# hipoteca

Calculadora de Hipoteca Inversa
Este programa es una aplicación web desarrollada con Flask que permite calcular diferentes tipos de hipotecas inversas. Una hipoteca inversa es un producto financiero destinado a personas mayores que les permite obtener un préstamo o crédito utilizando su vivienda como garantía.
Descripción
La Calculadora de Hipoteca Inversa permite al usuario ingresar información como el valor de la vivienda, la edad, la tasa de interés anual y la renta mensual deseada. Con estos datos, el programa calcula el saldo de la deuda según el tipo de hipoteca inversa seleccionada: temporal, vitalicia o única.
Tipos de Hipoteca Inversa

Temporal : En este tipo de hipoteca inversa, el usuario especifica el número de años durante los cuales desea recibir la renta mensual. El programa calcula el saldo de la deuda acumulada durante ese período.
Vitalicia : En este caso, el usuario proporciona su esperanza de vida, y el programa calcula el saldo de la deuda considerando que recibirá la renta mensual durante ese tiempo.
Única : En esta modalidad, el programa calcula el saldo de la deuda final y el número de meses necesarios para que la deuda alcance el valor total de la vivienda.

Los resultados calculados se guardan en una base de datos PostgreSQL y se muestran en una página web.
Estructura del Programa
El programa sigue la estructura de una aplicación web Flask y consta de los siguientes archivos:

App.py: Archivo principal que inicia la aplicación Flask y registra el blueprint main.
Controller.py: Contiene las rutas y la lógica principal de la aplicación, incluyendo la conexión a la base de datos y el manejo de formularios.
Modell.py: Defina la clase HipotecaInversaque contiene los métodos para calcular los diferentes tipos de hipotecas inversas.
Index.HTML: Plantilla HTML que muestra el formulario para ingresar los datos.
Resultado.HTML: Plantilla HTML que muestra los resultados calculados.

uso

Clona este repositorio o descarga los archivos.
Asegúrese de tener Flask y las dependencias necesarias instaladas.
Configure la conexión a la base de datos PostgreSQL en Controller.py.
Ejecute el archivo App.pypara iniciar la aplicación.
Acceda a la aplicación web en su navegador y siga las instrucciones para calcular los diferentes tipos de hipotecas inversas.

Créditos
Este programa fue creado por David Zabala y Valentina Carmona.
