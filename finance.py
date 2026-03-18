# finance.py

def adicionar_salario():
    return float(input("Adicionar salário: "))


def adicionar_gasto(gastos):
    gasto = float(input("Adicionar gasto: "))
    return gastos + gasto


def calcular_saldo(salario, gastos):
    return salario - gastos


def calcular_investimento(mensal, taxa, meses, saldo_inicial=0):
    """
    Calcula o crescimento de um investimento com aportes mensais
    e juros compostos.

    Parâmetros:
    mensal (float): valor investido por mês
    taxa (float): taxa de juros mensal (ex: 0.01 = 1%)
    meses (int): quantidade de meses
    saldo_inicial (float): valor já acumulado anteriormente

    Retorna:
    float: valor final acumulado
    """
    total = saldo_inicial

    for _ in range(meses):
        total += mensal
        total *= (1 + taxa)

    return total