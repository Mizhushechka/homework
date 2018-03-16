# -*- coding: utf-8 -*-
from wtforms_alchemy import ModelForm

from comments_blog_14.models import Article, Comments


# https://wtforms-alchemy.readthedocs.org/en/latest/introduction.html
class ArticleForm(ModelForm):
    class Meta:
        model = Article


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        include = [
            'article_id',
        ]
