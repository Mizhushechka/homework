# -*- coding: utf-8 -*-

from datetime import date

from comments_blog_14.app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.String(500), unique=True, nullable=False)
    date_created = db.Column(db.Date, default=date.today)

    def __str__(self):
            return "<Article\n(Title is:\n'%s', Content is:\n'%s')>" % (
                self.title, self.content)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(
        db.Integer,
        db.ForeignKey('article.id'),
        nullable=False,
        index=True
    )
    article = db.relationship(Article, foreign_keys=[article_id, ])
    comment = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
