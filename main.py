from finance import adicionar_salario, adicionar_gasto, calcular_saldo, simular_investimento

salario = 0
gastos = 0

while True:
    print("\n1 - Adicionar salário")
    print("2 - Adicionar gasto")
    print("3 - Ver saldo")
    print("4 - Ver resumo")
    print("5 - Simular investimento\n")
    print("6 - Sair")

    opcao = int(input("Escolha: "))
    print()

    if opcao == 1:
        salario = adicionar_salario()
        print("\n")

    elif opcao == 2:
        gastos = adicionar_gasto(gastos)
        print("\n")
    
    elif opcao == 3:
        saldo = calcular_saldo(salario, gastos)
        print(f"Saldo: R$ {saldo:.2f}\n")
        if saldo < 0:
            print("Você está no vermelho!\n")
    
    elif opcao == 4:
        saldo = calcular_saldo(salario, gastos)
        print(f"Salário: R$ {salario:.2f}")
        print(f"Gastos: R$ {gastos:.2f}")
        print(f"Saldo: R$ {saldo:.2f}\n")
        if saldo < 0:
            print("Você está no vermelho!\n")
    
    elif opcao == 5:
        simular_investimento()

    elif opcao == 6:
        print("Saindo...")
        break
    
    else:
        print("Opção inválida")