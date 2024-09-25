import os
os.system("cls || clear")

#Funções
def limpa_tela():
    os.system("cls || clear")

def cardapio_print():
    print("\n---CARDÁPIO---")
    for codigo in cardapio:
        print(f"{codigo} - {cardapio[codigo][0]}, R${cardapio[codigo][1]:.2f}")

def calcular_total(subtotal, forma_pagamento):
    if forma_pagamento == '1':
        desconto = subtotal * 0.10
        total = subtotal - desconto
        return total, f"R${desconto:.2f} de desconto"
    else:
        acrescimo = subtotal * 0.10
        total = subtotal + acrescimo
        return total, f"R${acrescimo:.2f} de acréscimo"

#Variaveis

cardapio = {
    1: ("Pizza", 25.00),
    2: ("Macarronada", 20.00),
    3: ("Hamburguer", 10.00),
    4: ("Lasanha", 24.00),
    5: ("Bolo", 30.00),
    6: ("Brigadeiro", 2.00),
    7: ("Esfirra", 5.00)
}

lista_pratos = []
subtotal = 0

#Primeiro processamento

while True:
    limpa_tela()
    cardapio_print()
    opcao_prato = int(input("\nDigite o número do prato (ou 0 para finalizar): "))
    
    if opcao_prato == 0:
        break
    elif opcao_prato in cardapio:
        lista_pratos.append(opcao_prato)
        subtotal += cardapio[opcao_prato][1]
    else:
        print("Código inválido! Tente novamente.")
        continue
    
    mais_pedidos = input("Deseja fazer outro pedido? (s/n): ").strip().lower()
    if mais_pedidos != 's':
        break
forma_pagamento = input("\nForma de pagamento (1 - À vista, 2 - Cartão de crédito): ")
total, desconto_str = calcular_total(subtotal, forma_pagamento)

#Exibindo para o usuario.

print("\n--- Resultado do Pedido ---")
print(f"Pratos escolhidos: {', '.join(str(cardapio[prato][0]) for prato in lista_pratos)}")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Forma de pagamento: {'À vista (10% de desconto)' if forma_pagamento == '1' else 'Cartão de crédito (10% de acréscimo)'}")
print(f"Valor aplicado: {desconto_str}")
print(f"Total a pagar: R${total:.2f}")
