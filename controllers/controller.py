from flask import Flask, render_template, request, redirect, url_for

from services import service

app = Flask(__name__)
service = service.Service()


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/pick', methods=['GET', 'POST'])
def pick():
    if request.method == 'GET':
        return render_template('pick.html')
    else:
        game_code = request.form.get('game_code')
        return redirect(url_for('game', code=game_code))


@app.route('/random', methods=['GET'])
def random():
    return redirect(url_for('game', code=service.get_random_game_code()))


@app.route('/game/<code>', methods=['GET', 'POST'])
def game(code):
    if request.method == 'GET':
        matrix = service.get_matrix(code)
        return render_template('game.html', game_code=code, game_matrix=matrix)
    else:
        # handle logic
        pass


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        # handle creation
        return redirect(url_for('created'))


@app.route('/created', methods=['GET'])
def created():
    return render_template('created.html')


@app.route('/finish', methods=['GET'])
def finish():
    return render_template('finish.html')


if __name__ == '__main__':
    app.run()
