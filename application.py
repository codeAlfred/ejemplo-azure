from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "hola mundo"

@app.route('/prueba')
def prueba():
    return render_template("prueba.html")


if __name__ == '__main__':
  app.run(port=80, debug=True)
