from twilio.rest import Client
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure suas credenciais da Twilio
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    from_number = request.form['From']
    message_body = request.form['Body']
    
    # Lógica simples para resposta
    response_message = "Oi! Me chamo Z, sou assistente virtual do Jeff. No momento ele está ocupado, mas já que você está aqui, aceita um cafezinho?"

    if "sim" in message_body.lower():
        response_message = "Que ótimo! Duas opções de café especial hoje: 1. Cafezinho 'Kalango': ... 2. Cafezinho 'Metal': ..."
    elif "não" in message_body.lower():
        response_message = "Ah, que pena. Mas tudo bem. Saiba que o convite ainda está de pé. Aguarde que já entraremos em contato."

    # Enviar resposta via Twilio
    client.messages.create(
        body=response_message,
        from_='whatsapp:+14155238886',  # Número de WhatsApp do Twilio
        to=from_number
    )
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(port=5000)
