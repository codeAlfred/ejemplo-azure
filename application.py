from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "hola mundo"

@app.route('/prueba')
def prueba():
    return "hola prueba como estas"


if __name__ == '__main__':
  app.run(port=80, debug=True)
