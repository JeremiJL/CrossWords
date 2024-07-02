import copy
from configparser import ConfigParser

from flask import Flask, render_template, request, redirect, url_for

from services.service import Service

service = Service()
app = Flask(__name__)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/pick', methods=['GET', 'POST'])
def pick():
    if request.method == 'GET':
        return render_template('pick.html')
    else:
        game_code = request.form.get('game_code')
        if service.check_code(game_code):
            return redirect(url_for('game', code=game_code))
        else:
            return redirect(url_for('error', message="There is no Puzzle with given ID"))


@app.route('/random', methods=['GET'])
def random():
    return redirect(url_for('game', code=service.get_random_game_code()))


@app.route('/game/<code>', methods=['GET', 'POST'])
def game(code):
    if request.method == 'GET':
        matrix = service.get_matrix(code)
        hints = service.get_hints(code)
        return render_template('game.html', game_code=code, game_matrix=matrix, game_hints=hints)
    else:
        result = request.form.values()
        complete = service.validate(result, code)
        print(complete)
        return render_template('finish.html', is_complete=complete)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    else:
        size = request.form.get('words_count')
        return redirect(url_for('customize', puzzle_size=size))


@app.route('/customize/<puzzle_size>', methods=['GET', 'POST'])
def customize(puzzle_size):
    if request.method == 'GET':
        return render_template('customize.html', puzzle_size=int(puzzle_size))
    else:
        words = list(request.form.values())
        result = service.check(copy.deepcopy(words))
        if result:
            game_id = service.save_puzzle(words)
            return render_template('created.html', status=result, game_id=game_id)
        else:
            return render_template('created.html', status=result)


@app.route('/created', methods=['GET'])
def created():
    return render_template('created.html')


@app.route('/finish', methods=['GET'])
def finish():
    return render_template('finish.html')


@app.route("/error/<message>", methods=['GET'])
def error(message):
    return render_template('error.html', error_message=message)


def get_port_from_config():
    # read configurations
    configur = ConfigParser()
    configur.read('configuration/config.ini')
    return int(configur.get('flask', 'port'))


if __name__ == '__main__':
    port = get_port_from_config()
    app.run(port=port)
