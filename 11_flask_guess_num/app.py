from flask import Flask, request, flash
import random
from flask_wtf import FlaskForm
from wtforms import IntegerField, validators
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.environ['S']
app.config['WTF_CSRF_ENABLED'] = False


class GuessForm(FlaskForm):
    guess = IntegerField(label='Guess', validators=[
        validators.InputRequired()
    ])


#S = 5
FLASK_RANDOM_SEED = app.config['SECRET_KEY']
random.seed(FLASK_RANDOM_SEED)
to_guess = random.randint(1, 10)


def guess_num(num_to_guess, users_guess):
    result = 0
    if num_to_guess == users_guess:
        result = "="
    if num_to_guess < users_guess:
        result = ">"
    if num_to_guess > users_guess:
        result = "<"
    print(result)
    return result


# для удобства перенесено на один url
@app.route('/guess', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'GET':
        print(to_guess)
        result = 'Число загадано'
    elif request.method == 'POST':
        form = GuessForm(request.form)
        if form.validate():
            guess_result = guess_num(form.guess.data, to_guess)
            flash(guess_result)
            result = guess_result
        else:
            flash('Form is not valid!')
            flash(str(form.errors))
    return result


if __name__ == '__main__':
    app.run()
