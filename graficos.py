# graficos.py

import matplotlib.pyplot as plt


def grafico_evolucao(simulacao):
    """
    Gera gráfico de crescimento mês a mês considerando juros compostos
    e múltiplas etapas de investimento.
    """
    valores = []
    meses_lista = []
    marcadores = []

    conta = 0
    mes_total = 0

    for etapa in simulacao["etapas"]:
        mensal = etapa["mensal"]
        taxa = etapa["taxa"]
        meses = etapa["meses"]

        # Simulação mês a mês (núcleo do cálculo financeiro)
        for _ in range(meses):
            conta = (conta + mensal) * (1 + taxa)
            mes_total += 1

            valores.append(conta)
            meses_lista.append(mes_total)

        # Marca visual onde há mudança de etapa
        marcadores.append(mes_total)

    plt.figure(figsize=(10, 5))
    plt.plot(meses_lista, valores)

    for m in marcadores:
        plt.axvline(x=m, linestyle='--')

    plt.text(meses_lista[-1], valores[-1], f"{valores[-1]:.2f}")

    plt.xlabel("Meses")
    plt.ylabel("Dinheiro (R$)")
    plt.title("Evolução do Investimento (Juros Compostos)")

    plt.grid()
    plt.savefig("assets/exemplo_grafico.png")
    plt.show()


def grafico_comparacao(simulacao):
    """Compara total investido com valor final acumulado."""
    investido = simulacao["total_investido"]
    final = simulacao["total_final"]

    categorias = ["Investido", "Final"]
    valores = [investido, final]

    plt.figure()
    plt.bar(categorias, valores)

    lucro = final - investido
    plt.title(f"Investido vs Final (Lucro: R$ {lucro:.2f})")
    plt.ylabel("Valor (R$)")

    for i, valor in enumerate(valores):
        plt.text(i, valor, f"{valor:.2f}", ha='center', va='bottom')

    plt.show()