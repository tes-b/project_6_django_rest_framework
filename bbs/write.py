from django import forms
from bbs.models import Board


class PostForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('id', 'title', 'contents')