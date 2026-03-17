#finance.py

def adicionar_salario():
    return float(input("Adicionar salário: "))


def adicionar_gasto(gastos):
    gasto = float(input("Adicionar gasto: "))
    return gastos + gasto


def calcular_saldo(salario, gastos):
    return salario - gastos

def simular_investimento():
    invest_mes = 0.0
    tempo = 0
    conta = 0.0
    total_invest = 0.0
    tempo_total = 0
    op = 's'
    while op != 'n':
        invest_mes = float(input("Quanto você quer investir: "))
        tempo = int(input("Quantidade de meses investindo: "))
        tempo_total += tempo
        for i in range(tempo):
            conta += invest_mes + conta * 0.01
        total_invest += invest_mes * tempo
        print(f"\nTotal final: R$ {conta:.2f}")
        print(f"Total investido: R$ {total_invest:.2f}")
        print(f"Tempo investido: {tempo_total/12:.0f} ano(s) e " f"{tempo_total%12:.0f} mes(es)")
        print(f"Valorizou: R$ {conta-total_invest:.2f}\n")
        op = input("Quer continuar investindo?(s/n): ")
