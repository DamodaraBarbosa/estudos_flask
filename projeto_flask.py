from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def saudation():
    return '<h1>Olá, gamers!</h1>'

app.run()