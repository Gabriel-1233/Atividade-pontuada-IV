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
#Funções
import os
os.system("cls || clear")    

def limpa_tela():
    os.system("cls || clear")    

def opcao_primeira():
    print("""
O cliente deseja fazer mais pedidos?
1-Sim eu quero!
2-Não eu não quero!
Considere que os preços dos pratos serão somados.""")
    
def cardapio_print():
    print("""
---Prato---
1-Picanha R$25.00
2-Lasanha R$20.00
3-Strogonoff R$18.00
4-Bife Acebolado R$15.00
5-Pão com ovos R$5.00
6-Macarronada R$17.00
7-Pizza R$ 50.00 
""")

def cardapio():
    picanha=25.00
    Lasanha=20.00
    Strogonoff=18.00
    Bife_Acebolado=15.00
    Pão_com_ovo=5.00
    Macarronada=17.00
    Pizza=50.00
    return picanha,Lasanha,Strogonoff,Bife_Acebolado,Pão_com_ovo,Macarronada,Pizza

def acumulador_valores(lista_resultado):
    soma=0
    for resultado in lista_resultado:
            soma+=opcao
            resultado=soma
            return resultado
#valor dos pratos
picanha=25.00
Lasanha=20.00
Strogonoff=18.00
Bife_Acebolado=15.00
Pão_com_ovo=5.00
Macarronada=17.00
Pizza=50.00
#variaveis(constantes e vetores)
lista_pratos=[]
QUANTIDADE=7
lista_resultado=[]
lista_comidas=cardapio()
avista=0.1

#Entrada
cardapio_print()
opcao_prato=int(input("Digite o numero do prato: "))
limpa_tela()
#exibindo ao usuario
match(opcao_prato):
    case 1:

        print("""
O cliente deseja fazer mais pedidos?
1-Sim eu quero!
2-Não eu não quero!
Considere que os preços dos pratos serão somados.""")
        opcao=int(input("Digite a opção escolhida:"))
        limpa_tela()
        match(opcao):
            case 1:
                while True:
                    picanha=25.00
                    Lasanha=20.00
                    Strogonoff=18.00
                    Bife_Acebolado=15.00
                    Pão_com_ovo=5.00
                    Macarronada=17.00
                    Pizza=50.00
                    
                    print("Lembre-se que para parar de pedir pratos digite 0!")
                    opcao=int(input("Digite o prato escolhido:"))
                    limpa_tela()
                    soma=0
                    if opcao==0:
                        soma+=opcao
                        soma_total=soma
                        desconto=soma_total*0.1
                        print(f"O total deu:{desconto}")
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
                            print(f"--Picanha--")
                            print(f"O prato que você escolheu custa: {picanha}")
                            break
                    case 2:
                            print(f"--Lasanha--")
                            print(f"O preço do prato escolhido é: {Lasanha}")
                            break
                    case 3:
                            print(f"--Strogonoff--")
                            print(f"O preço do prato escolhido é: {Strogonoff}")
                            break
                    case 4:
                            print(f"--Bife Acebolado--")
                            print(f"O preço do prato escolhido é: {Bife_Acebolado}")
                            break
                    case 5:
                            print(f"--Pão com ovos--")
                            print(f"O preço do prato escolhido é: {Pão_com_ovo}")
                            break
                    case 6:
                            print(f"--Macarronada--")
                            print(f"O preço do prato escolhido é: {Macarronada}")
                    case 7:
                            print(f"--Pizza--")
                            print(f"O preço do prato escolhido é: {Pizza}")