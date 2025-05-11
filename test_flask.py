from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask fonctionne !'

if __name__ == '__main__':
    print(">>> Flask démarre...")
    app.run(host='0.0.0.0', port=10000, debug=True)
