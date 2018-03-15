# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa


app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret',

    # Database settings:
    SQLALCHEMY_DATABASE_URI='sqlite:///people.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    WTF_CSRF_ENABLED=False
)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/items', methods=['GET', 'POST'])
def index():
    from posts.forms import GuestBookForm
    from posts.models import GuestBookItem

    posts = GuestBookItem.query.all()
    if request.method == 'GET':
        return jsonify([p.to_dict() for p in posts])

    if request.method == 'POST':
        # import ipdb; ipdb.set_trace();
        print(request.form)
        form = GuestBookForm(request.form)

        if form.validate():
            post = GuestBookItem(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    return render_template('home.txt', posts=posts)


if __name__ == '__main__':
    from posts.models import *
    db.create_all()
    app.run()
