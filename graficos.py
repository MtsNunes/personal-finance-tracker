import matplotlib.pyplot as plt

def grafico_evolucao(simulacao):
    valores = []
    meses_lista = []
    marcadores = []

    conta = 0
    mes_total = 0

    for etapa in simulacao["etapas"]:
        mensal = etapa["mensal"]
        taxa = etapa["taxa"]
        meses = etapa["meses"]

        for _ in range(meses):
            conta = (conta + mensal) * (1 + taxa)

            mes_total += 1
            valores.append(conta)
            meses_lista.append(mes_total)

        marcadores.append(mes_total)

    plt.figure(figsize=(10, 5))
    plt.plot(meses_lista, valores)

    # linhas de mudança de etapa
    for m in marcadores:
        plt.axvline(x=m, linestyle='--')

    # valor final
    plt.text(meses_lista[-1], valores[-1], f"{valores[-1]:.2f}")

    plt.xlabel("Meses")
    plt.ylabel("Dinheiro (R$)")
    plt.title("Evolução do Investimento (Juros Compostos)")

    plt.grid()
    plt.savefig("assets/exemplo_grafico.png")
    plt.show()

def grafico_comparacao(simulacao):
    investido = simulacao["total_investido"]
    final = simulacao["total_final"]

    categorias = ["Investido", "Final"]
    valores = [investido, final]

    plt.figure()
    plt.bar(categorias, valores)

    lucro = final - investido

    plt.title(f"Investido vs Final (Lucro: R$ {lucro:.2f})")
    plt.ylabel("Valor (R$)")

    # valores nas barras
    for i, valor in enumerate(valores):
        plt.text(i, valor, f"{valor:.2f}", ha='center', va='bottom')

    plt.show()