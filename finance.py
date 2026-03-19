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
    Simula investimento com aportes mensais e juros compostos.

    A cada mês:
    1. adiciona o aporte
    2. aplica a taxa de juros

    Mantém continuidade com saldo inicial (importante para múltiplas etapas).
    """
    total = saldo_inicial

    for _ in range(meses):
        total += mensal
        total *= (1 + taxa)

    return total