import os
import platform

def clear_screen():
    # Limpar a tela de acordo com o sistema operacional
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear_screen()  # Limpar a tela antes de mostrar as boas-vindas

    print("Oi! Me chamo Z, sou assistente virtual do Jeff.")
    print("No momento ele está ocupado, mas já que você está aqui, aceita um cafezinho?")

    resposta = input("Por favor, 'sim' ou 'não': ").strip().lower()
    if resposta != "sim":
        print("Ah, que pena. Mas tudo bem. Saiba que o convite ainda está de pé. Aguarde que já entraremos em contato.")
        return

    # Descrição dos Produtos
    print("\nQue ótimo!")
    print("\nDuas opções de café especial hoje:")
    print("1. Cafezinho \"Kalango\": Catuai Vermelho 144, Altitude 1006 metros, Aroma de frutas tropicais, Sabor de mel e cacau.")
    print("2. Cafezinho \"Metal\": Variedade Duvidosa, Aroma de rock pauleira, Sabor de fruto proibido.")

    # Pergunta sobre quantidade
    try:
        quantidade_kalango = int(input("\nEntão, quantos sachês do Cafezinho \"Kalango\" você gostaria de levar? "))
        quantidade_metal = int(input("Blz. Quantos sachês do Cafezinho \"Metal\" você gostaria de presentear um amigo? "))
    except ValueError:
        print("Por favor, insira números válidos.")
        return

   

    # Oferta de adesivo surpresa
    if quantidade_kalango > 0 and quantidade_metal > 0:
        print("Ambos? Que legal! Você ganhou um adesivo super maneiro! 🎁")

     # Cálculo do total
    total = (quantidade_kalango + quantidade_metal) * 5
    print(f"\nTotal: R$ {total}.00")

    # Confirmação do pedido
    confirmacao = input("Você gostaria de confirmar o pedido? (sim/não): ").strip().lower()
    if confirmacao == "sim":
        print("\nPedido confirmado! Obrigado pela sua compra! Entraremos em contato para finalizar o pagamento e o envio.")
    else:
        print("\nTudo bem! Aguarde que já entraremos em contato. Até logo!")

if __name__ == "__main__":
    main()
