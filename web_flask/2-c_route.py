from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def cis(text):
    text = text.replace("_", " ")
    return f"C {text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)