#finance.py

def adicionar_salario():
    return float(input("Adicionar salário: "))


def adicionar_gasto(gastos):
    gasto = float(input("Adicionar gasto: "))
    return gastos + gasto


def calcular_saldo(salario, gastos):
    return salario - gastos