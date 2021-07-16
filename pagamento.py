
def pagamento(*args):
    
    if opcao != "C" and opcao != "F":
            print("Digite uma opção válida para continuar!")

    if opcao == "F":

        pagamento = str(input("Digite uma opção para forma de pagamento? \n" +
        "*1* ==> Crédito \n" +
        "*2* ==> Débito \n" +
        "*3* ==> Dinheiro "))
        if pagamento == "2" or pagamento =="3":
            pagamento = pagamento - pagamento*5/100
            pagamento = sum(lista_valor_produto)
            print(lista_nome_produto)
            print(pagamento)

        if pagamento == "1":
            pagamento = sum(lista_valor_produto)
            print(lista_nome_produto)
            print(pagamento)

        else:
            print("Digite uma opção válida!")
        continue