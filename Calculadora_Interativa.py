def calculadora(opcao_1, opcao_2, operacao):
    if operacao == 1:
        solucao = opcao_1 + opcao_2
    elif operacao == 2:
        solucao = opcao_1 - opcao_2
    elif operacao == 3:
        solucao = opcao_1 * opcao_2
    elif operacao == 4:
        if opcao_2 != 0: 
            solucao = opcao_1 / opcao_2
        else:
            solucao = "Erro: divisão por zero!"  
    else:
        solucao = "Erro: operação inválida!" 
    return solucao

def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Por favor, insira um número válido.")

def calculadora_interativa():
    while True:
        print("\nBem-vindo à Calculadora Cloud Talent!")
        print("Selecione a operação desejada:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = input("Selecione uma das opções acima ")
        if operacao == '0':
            print("Obrigado por usar a Calculadora Interativa. Até logo!")
            break
        elif operacao in ['1', '2', '3', '4']:
            operacao = int(operacao)
        else:
            print("Essa opção não existe.")
            continue

        opcao_1 = ler_numero("Digite o primeiro número: ")
        opcao_2 = ler_numero("Digite o segundo número: ")

        solucao = calculadora(opcao_1, opcao_2, operacao)

        print("Resultado da Operação é --->", solucao)

calculadora_interativa()

