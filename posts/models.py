# -*- coding: utf-8 -*-

from datetime import date


from posts.app import db


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(80), unique=True, nullable=False)
    # title = db.Column(db.String(140), unique=True, nullable=False)
    article = db.Column(db.String(5000), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    to_delete = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'article': self.article,
            'date_created': self.date_created,
            'to_delete': self.to_delete,
        }
