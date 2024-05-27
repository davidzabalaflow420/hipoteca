class HipotecaInversa:
    """
    Clase que representa una hipoteca inversa, un tipo de préstamo en el cual
    el prestamista hace pagos al prestatario en lugar de que el prestatario
    realice pagos al prestamista. Esta clase permite calcular el saldo de
    la deuda en diferentes escenarios de hipoteca inversa.
    """

    def __init__(self, valor_vivienda, edad, interes_anual, renta_mensual):
        """
        Inicializa una instancia de HipotecaInversa.

        Args:
        - valor_vivienda (float): El valor total de la vivienda.
        - edad (int): La edad del prestatario.
        - interes_anual (float): La tasa de interés anual (en porcentaje).
        - renta_mensual (float): El monto de la renta mensual pagada al prestatario.
        """
        self.valor_vivienda = valor_vivienda
        self.edad = edad
        self.interes_anual = interes_anual
        self.renta_mensual = renta_mensual

    def hipoteca_inversa_temporal(self, años):
        """
        Calcula el saldo de la deuda en un escenario de hipoteca inversa temporal.

        Args:
        - años (int): El número de años de la hipoteca inversa.

        Returns:
        - float: El saldo de la deuda después del período de tiempo especificado.
        """
        total_rentas = años * 12 * self.renta_mensual
        interes_mensual = self.interes_anual / 12 / 100
        deuda = 0
        for _ in range(años * 12):
            deuda = deuda * (1 + interes_mensual) + self.renta_mensual
        return min(total_rentas, deuda)

    def hipoteca_inversa_vitalicia(self, esperanza_vida):
        """
        Calcula el saldo de la deuda en un escenario de hipoteca inversa vitalicia.

        Args:
        - esperanza_vida (int): La esperanza de vida del prestatario en años.

        Returns:
        - float: El saldo de la deuda considerando la esperanza de vida del prestatario.
        """
        total_rentas = esperanza_vida * 12 * self.renta_mensual
        interes_mensual = self.interes_anual / 12 / 100
        deuda = 0
        for _ in range(esperanza_vida * 12):
            deuda = deuda * (1 + interes_mensual) + self.renta_mensual
        return min(total_rentas, deuda)

    def hipoteca_inversa_unica(self):
        """
        Calcula el saldo de la deuda en un escenario de hipoteca inversa única.

        Returns:
        - tuple: Una tupla que contiene el saldo de la deuda final y el número de meses
        necesarios para que la deuda alcance el valor total de la vivienda.
        """
        interes_mensual = self.interes_anual / 12 / 100
        deuda = 0
        meses = 1
        while deuda < self.valor_vivienda:
            deuda = deuda * (1 + interes_mensual) + self.renta_mensual
            meses += 1
        return deuda, meses
