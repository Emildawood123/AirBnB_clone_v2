from flask import Flask, abort, render_template

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

@app.route('/python/')
def python():
    return "Python is cool"

@app.route('/python/<text>')
def pythonis(text):
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route('/number/<n>')
def number(n):
    try:
        n = int(n)
        return f"{n} is number"
    except:
        abort(404)

@app.route('/number_template/<n>')
def number_tamplete(n):
    try:
        n = int(n)
        return render_template('5-number.html', number=n)
    except:
        abort(404)

@app.route('/number_odd_or_even/<n>')
def number_even_odd(n):
    try:
        n = int(n)
        return render_template('6-number_odd_or_even.html', number=n)
    except:
        abort(404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)