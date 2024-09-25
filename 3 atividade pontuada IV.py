"""
Exibir um menu com 7 pratos, apresentando o código do prato e o nome.
O usuário poderá inserir o código do prato desejado. Caso o código seja inválido, o sistema deve alertar o usuário e pedir novamente um código válido.

O sistema deverá perguntar ao usuário se ele deseja fazer outro pedido e, se sim, permitir a adição de mais pratos ao pedido.

Acumular os valores de cada prato escolhido.

Se o usuário digitar o código "0", o programa encerrará o pedido e calculará o valor total.
O sistema deve solicitar a forma de pagamento:
À vista (desconto de 10% sobre o valor total).
Cartão de crédito (acréscimo de 10% sobre o valor total).
Exibir os resultados ao final:
A lista com os códigos e nomes dos pratos escolhidos.
O subtotal (valor total sem acréscimo ou desconto).
A forma de pagamento escolhida.
O valor do desconto ou acréscimo aplicado.
O valor final a ser pago."""
import os
os.system("cls || clear")

#Funções
def limpa_tela():
    os.system("cls || clear")    

def cardapio_print():
    print("""
    ---CARDAPIO---
1-Pizza, 25.00
2-Macarronada, 20.00
3-Hamburguer, 10.00
4-Lasanha, 24.00
5-Bolo, 30.00
6-Brigadeiro, 2.00
7-Esfirra, 5.00
""")

#Primeira declaração
Pizza=25.00
Macarronada=20.00
Hamburguer=10.00
Lasanha=24.00
Bolo=30.00
Brigadeiro=2.00
Esfirra=5.00

#Variaveis(constantes,listas).
lista_pratos=[]
#Primeira solicitação
cardapio_print()
opcao_prato=int(input("Digite o numero do prato: "))

match(opcao_prato):
    case 1:
        print("""
O cliente deseja fazer mais pedidos?
1-Sim eu quero!
2-Não eu não quero!
Considere que os preços dos pratos serão somados.""")
        while True:
            opcao=int(input("Digite a opção escolhida:"))
            limpa_tela()
            if (opcao!=1,2,0):
                print("O senhor está digitando uma opção inexistente!")
                limpa_tela()
            else:
                break
        match(opcao):
                 case 1:
                    picanha=25.00
                    Lasanha=20.00
                    Strogonoff=18.00
                    Bife_Acebolado=15.00
                    Pão_com_ovo=5.00
                    Macarronada=17.00
                    Pizza=50.00
                 case 0:
                    picanha=25.00
                    Lasanha=20.00
                    Strogonoff=18.00
                    Bife_Acebolado=15.00
                    Pão_com_ovo=5.00
                    Macarronada=17.00
                    Pizza=50.00
                    
                    print("Obrigado por escolher a nós e não nossos rivais!")
                    print(f"O valor do prato que o senhor quer:{opcao}")
    case _:
        while True:
            if (opcao_prato<=0) or (opcao_prato>7):  
                cardapio_print()
                print(f"Você escolheu um opção inesistente!")
                opcao_prato=int(input("Digite o numero do prato: "))
                limpa_tela()
            else:
                match(opcao_prato):
                    case 1:
                            print(f"--Pizza--")
                            print(f"O prato que você escolheu custa: {Pizza}")
                            break
                    case 2:
                            print(f"--Macarronada--")
                            print(f"O preço do prato escolhido é: {Macarronada}")
                            break
                    case 3:
                            print(f"--Hamburguer--")
                            print(f"O preço do prato escolhido é: {Hamburguer}")
                            break
                    case 4:
                            print(f"--Lasanha--")
                            print(f"O preço do prato escolhido é: {Lasanha}")
                            break
                    case 5:
                            print(f"--Bolo--")
                            print(f"O preço do prato escolhido é: {Bolo}")
                            break
                    case 6:
                            print(f"--Brigadeiro--")
                            print(f"O preço do prato escolhido é: {Brigadeiro}")
                    case 7:
                            print(f"--Esfirra--")
                            print(f"O preço do prato escolhido é: {Esfirra}")
