from django.contrib.auth.models import User
from django import forms
from .models import Users
#회원가입 양식폼 

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['id', 'password', 'name',
                  'age', 'gender', 'email']

#clean_method=> form 안에서 validation 거친 뒤 검증된 후의 적당한 데이터가 들어있는 변수
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched')
        return cd['password']
    
# hex(aes_encrypy(password, 'key')) -> encode
# aes_decrypt(unhex(password), 'key') -> decode        
