# -*- coding: utf-8 -*-
from wtforms_alchemy import ModelForm

from posts.models import GuestBookItem


# https://wtforms-alchemy.readthedocs.org/en/latest/introduction.html
class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBookItem


# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         include = [
#             'user_id',
#         ]