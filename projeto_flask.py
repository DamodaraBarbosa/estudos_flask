from flask import Flask,render_template, request

class Jogo:
    def __init__(self, nome, genero, plataforma) -> None:
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma

jogo1 = Jogo('Halo Infinite', 'FPS', 'Xbox')
jogo2 = Jogo('Horizon Forbiden West', 'Ação & Aventura', 'Playstation')
jogo3 = Jogo('Mario Odyssey', 'Plataforma', 'Nintendo')

lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)

@app.route('/inicio')
def saudation():
    return render_template('lista.html', titulo= 'Jogos', jogos= lista_jogos)

@app.route('/novogame')
def new_game():
    return render_template('new_game.html', titulo= 'Cadastro de jogos')

@app.route('/criar', methods= ['POST', ] )
def criar():
    nome = request.form['nome']
    genero = request.form['categoria']
    plataforma = request.form['console']

    jogo =  Jogo(nome, genero, plataforma)

    lista_jogos.append(jogo)
    render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

app.run()