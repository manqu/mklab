from django import forms
from shop.models import Comment
from django.db import models
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', ]
        #exclude = ['content_type', 'object_id',]

        def __init__(self):
            pass
            #return request.user
