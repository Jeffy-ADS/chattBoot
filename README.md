# Assistente Virtual "Z" - Café Virtual

Este projeto é um simples script Python que simula uma interação com um assistente virtual chamado "Z". O assistente faz uma oferta de café especial e guia o usuário através de um processo de compra fictício. O código é ideal para quem deseja aprender sobre interatividade em scripts Python ou criar uma interface de terminal amigável.

## Funcionalidades

- **Limpeza de Tela:** O script limpa a tela do terminal antes de iniciar a interação, adaptando-se ao sistema operacional (Windows, Linux, macOS).
- **Interação com o Usuário:** O assistente virtual "Z" cumprimenta o usuário e oferece duas opções de café.
- **Entrada de Dados:** O usuário pode escolher quantos sachês de cada café deseja comprar.
- **Brinde Surpresa:** Se o usuário comprar ambos os tipos de café, ele recebe um adesivo como brinde.
- **Cálculo de Total:** O total da compra é calculado e exibido.
- **Confirmação do Pedido:** O usuário pode confirmar ou cancelar a compra.

## Como Usar

1. **Pré-requisitos:**
   - Python 3.x instalado no sistema.
   - Um terminal (ou console) para executar o script.

2. **Execução:**
   - Clone ou baixe este repositório em sua máquina.
   - Abra o terminal no diretório onde o script está localizado.
   - Execute o script com o comando:
     ```bash
     python nome_do_arquivo.py
     ```
   - O assistente "Z" iniciará a interação.

3. **Interação:**
   - Responda às perguntas que o assistente "Z" faz no terminal.
   - Insira números válidos quando solicitado.
   - No final, confirme ou cancele o pedido.

## Estrutura do Código

### Funções Principais

- **clear_screen():** 
  Limpa a tela do terminal dependendo do sistema operacional.

- **main():**
  A função principal que controla o fluxo do programa, incluindo a interação com o usuário e a lógica de negócio.

### Exemplo de Execução

```bash
Oi! Me chamo Z, sou assistente virtual do Jeff.
No momento ele está ocupado, mas já que você está aqui, aceita um cafezinho?
Por favor, 'sim' ou 'não': sim

Que ótimo!

Duas opções de café especial hoje:
1. Cafezinho "Kalango": Catuai Vermelho 144, Altitude 1006 metros, Aroma de frutas tropicais, Sabor de mel e cacau.
2. Cafezinho "Metal": Variedade Duvidosa, Aroma de rock pauleira, Sabor de fruto proibido.

Então, quantos sachês do Cafezinho "Kalango" você gostaria de levar? 3
Blz. Quantos sachês do Cafezinho "Metal" você gostaria de presentear um amigo? 2

Ambos? Que legal! Você ganhou um adesivo super maneiro! 🎁

Total: R$ 25.00
Você gostaria de confirmar o pedido? (sim/não): sim

Pedido confirmado! Obrigado pela sua compra! Entraremos em contato para finalizar o pagamento e o envio.
