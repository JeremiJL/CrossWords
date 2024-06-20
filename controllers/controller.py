from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_home():
    return render_template('home.html')


@app.route('/game')
def get_game():
    return render_template('game.html')


if __name__ == '__main__':
    app.run()
