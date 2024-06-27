from flask import Flask, render_template, request, redirect, url_for
from repositories import repository
from gameplay.brain import Brain

app = Flask(__name__)
brain = None

@app.route('/')
def get_home():
    return render_template('home.html')


@app.route("/pick", methods = ['POST', 'GET'])
def get_pick():
    if request.method == 'GET':
        return render_template('pick.html')
    else:
        puzzleId = request.form['puzzleId']
        pass
        # return redirect(url_for('get_game', pId=puzzleId))


# @app.route('/get_game/<pId>')
# def get_game(pId):
#     puzzle = service.get_puzzle(pId)
#     brain = Brain(puzzle)
#     return render_template('game.html', matrix = brain.logic_matrix)


if __name__ == '__main__':
    service.connect()
    app.run()
