from django import forms
from bbs.models import Board


class PostForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('id', 'title', 'contents')
        widgets = {
            'title': forms.TextInput(
                attrs={'style':'width: 90%','placeholder':'제목을 입력하세요.'}
            ),
            'contents':forms.Textarea(
                attrs={'style':'width: 90%; height:50vh;'}
            )
        }