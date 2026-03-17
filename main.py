from finance import adicionar_salario, adicionar_gasto, calcular_saldo

salario = 0
gastos = 0

while True:
    print("\n1 - Adicionar salário")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Sair")
    print("5 - Ver resumo")

    opcao = int(input("Escolha: "))

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
        print("Saindo...")
        break
    elif opcao == 5:
        saldo = calcular_saldo(salario, gastos)
        print(f"Salário: R$ {salario:.2f}")
        print(f"Gastos: R$ {gastos:.2f}")
        print(f"Saldo: R$ {saldo:.2f}")
        if saldo < 0:
            print("Você está no vermelho!")
    else:
        print("Opção inválida")