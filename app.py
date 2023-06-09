from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/user')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)