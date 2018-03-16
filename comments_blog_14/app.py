# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config as config


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)

@app.route('/create', methods=['POST'])
def index():
    from comments_blog_14.forms import ArticleForm
    from comments_blog_14.models import Article

    form = ArticleForm(request.form)

    if form.validate():
        post = Article(**form.data)
        db.session.add(post)
        db.session.commit()

        flash('Post created!')

        result = 'Ok'
    else:
        flash('Form is not valid! Post was not created.')
        flash(str(form.errors))

        result = 'not Ok'
    return result

@app.route('/comment', methods=['GET', 'POST'])
def index_comm():
    from comments_blog_14.forms import CommentsForm
    from comments_blog_14.models import Article

    result = 0
    if request.method == 'GET':
        posts = Article.query.all()
        for post in posts:
            result = render_template('articles.txt', posts=posts)

    if request.method == 'POST':
        form = CommentsForm(request.form)
        if form.validate():
            comment = Comments(**form.data)
            db.session.add(comment)
            db.session.commit()

            flash('Comment created!')
            result = 'Ok'

        else:
            flash('Form is not valid! Comment was not created.')
            flash(str(form.errors))
            result = ' not Ok'
    return result


#   return render_template('home.txt', posts=posts)


if __name__ == '__main__':
    from comments_blog_14.models import *
    db.create_all()
    app.run()
