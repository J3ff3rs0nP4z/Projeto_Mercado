import os
os.system('cls')
import csv

print("#####  LISTA DE COMPRAS   #####")


opcao = str(input("SEJA BEM VINDO AO MERCADO DO POVO! \n" +
                "Digite uma ação para continuar: \n" + 
                    "** C ** ===> Comprar  \n" +
                    "** F ** ===> Finalizar a compra \n")).upper

if opcao != "C" and opcao != "F":
    print("Digite uma opção válida")

if opcao == "F":
    print("Você não comprou nada!!Volte Sempre!!!")



lista_nome_produto = []
lista_valor_produto = []

if opcao == "C":
    while True:

        nome_produto = str(input("Digite o produto: ")).lower()
        lista_nome_produto.append(nome_produto)

        valor_produto = float(input("Qual valor do produto R$"))
        lista_valor_produto.append(valor_produto)

        opcao = str(input("Digite uma ação para continuar: \n" + 
                        "** C ** ===> Comprar  \n" +
                        "** F ** ===> Finalizar a compra \n" + " ")
        
        if opcao ==  "C":
            continue
