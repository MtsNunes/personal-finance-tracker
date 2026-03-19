from finance import adicionar_salario, adicionar_gasto, calcular_saldo, calcular_investimento
import json
from graficos import grafico_evolucao, grafico_comparacao

# =========================
# JSON
# =========================
def salvar_historico(historico):
    with open("historico.json", "w") as arquivo:
        json.dump(historico, arquivo, indent=4)

def carregar_historico():
    try:
        with open("historico.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# =========================
# VARIÁVEIS
# =========================
salario = 0
gastos = 0

historico = carregar_historico()

# =========================
# LOOP PRINCIPAL
# =========================
while True:
    print("\n1 - Adicionar salário")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Ver resumo")
    print("5 - Nova simulação de investimento")
    print("6 - Ver histórico de investimentos")
    print("7 - Ver gráficos de uma simulação")
    print("8 - Sair\n")

    try:
        opcao = int(input("Escolha: "))
    except:
        print("Entrada inválida")
        continue

    # =========================
    # SALÁRIO / GASTOS
    # =========================
    if opcao == 1:
        salario = adicionar_salario()

    elif opcao == 2:
        gastos = adicionar_gasto(gastos)

    elif opcao == 3:
        saldo = calcular_saldo(salario, gastos)
        print(f"Saldo: R$ {saldo:.2f}")
        if saldo < 0:
            print("Você está no vermelho!")

    elif opcao == 4:
        saldo = calcular_saldo(salario, gastos)
        print(f"Salário: R$ {salario:.2f}")
        print(f"Gastos: R$ {gastos:.2f}")
        print(f"Saldo: R$ {saldo:.2f}")
        if saldo < 0:
            print("Você está no vermelho!")

    # =========================
    # NOVA SIMULAÇÃO
    # =========================
    elif opcao == 5:
        conta = 0
        total_invest = 0
        tempo_total = 0

        etapas = []

        print("\n--- NOVA SIMULAÇÃO INICIADA ---")

        op = 's'
        while op == 's':
            try:
                mensal = float(input("Quanto você quer investir: "))
                meses = int(input("Quantidade de meses: "))
                taxa = float(input("Taxa mensal (ex: 0.01): "))
            except:
                print("Entrada inválida\n")
                continue

            antes = conta

            # 🔥 AGORA PASSANDO A CONTA (continuidade real)
            conta = calcular_investimento(mensal, taxa, meses, conta)

            investido = mensal * meses
            ganho = conta - antes - investido

            total_invest += investido
            tempo_total += meses

            # salva etapa
            etapas.append({
                "mensal": mensal,
                "meses": meses,
                "taxa": taxa,
                "investido": investido,
                "ganho": ganho,
                "total_apos_etapa": conta
            })

            print("\n--- RESULTADO DA ETAPA ---")
            print(f"Total atual: R$ {conta:.2f}")
            print(f"Total investido: R$ {total_invest:.2f}")
            print(f"Tempo: {tempo_total//12} ano(s) e {tempo_total%12} mes(es)")
            print(f"Valorização: R$ {conta - total_invest:.2f}")
            print(f"Taxa: {taxa*100:.2f}% ao mês\n")

            op = input("Adicionar outra etapa? (s/n): ").lower()
            while op not in ['s', 'n']:
                op = input("Digite apenas s ou n: ").lower()

        # 🔥 salva simulação completa
        historico.append({
            "total_final": conta,
            "total_investido": total_invest,
            "tempo_total_meses": tempo_total,
            "etapas": etapas
        })

        salvar_historico(historico)
        print("\n✅ Simulação salva com sucesso!\n")

    # =========================
    # HISTÓRICO
    # =========================
    elif opcao == 6:
        if not historico:
            print("Nenhuma simulação encontrada.\n")
        else:
            for i, sim in enumerate(historico):
                print(f"\n====== SIMULAÇÃO {i+1} ======")
                print(f"Total final: R$ {sim['total_final']:.2f}")
                print(f"Total investido: R$ {sim['total_investido']:.2f}")
                print(f"Tempo: {sim['tempo_total_meses']//12} ano(s)")

                print("\n-- Etapas --")
                for j, etapa in enumerate(sim["etapas"]):
                    print(f"\nEtapa {j+1}")
                    print(f"Mensal: {etapa['mensal']}")
                    print(f"Meses: {etapa['meses']}")
                    print(f"Taxa: {etapa['taxa']}")
                    print(f"Investido: {etapa['investido']:.2f}")
                    print(f"Ganho: {etapa['ganho']:.2f}")
                    print(f"Total após etapa: {etapa['total_apos_etapa']:.2f}")

    elif opcao == 7:
        if not historico:
            print("Nenhuma simulação encontrada.\n")
        else:
            for i, sim in enumerate(historico):
                print(f"{i+1} - Simulação {i+1}")

            try:
                escolha = int(input("Escolha a simulação: ")) - 1
                simulacao = historico[escolha]
            except:
                print("Escolha inválida")
                continue

            print("\n1 - Evolução do investimento")
            print("2 - Comparação investido vs final")

            tipo = int(input("Escolha o gráfico: "))

            if tipo == 1:
                grafico_evolucao(simulacao)
            elif tipo == 2:
                grafico_comparacao(simulacao)
            else:
                print("Opção inválida")

    elif opcao == 8:
        print("Saindo...")
        break

    else:
        print("Opção inválida")