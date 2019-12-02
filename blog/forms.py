# -*- coding: utf-8 -*-
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

