from django.shortcuts import render
from .forms import RegisterForm



#회원가입 기능
def register(request):
    if request.method == 'POST':
        user_form= RegisterForm(request.POST) #forms.py에서 가져온 형식
        if user_form.is_valid():
            new_user = user_form.save() #비밀번호 데이터상 저장 x, commit=False시 메모리만 할당
            # new_user.set_password(user_form.cleaned_data['password']) #비밀번호 암호화
            # new_user.save() #원래 User 클래스 사용시 ->set_password 써서 암호화 시킨다음 저장함


            return render(request, 'registration/register_done.html',{'new_user':new_user})
    else:
            user_form = RegisterForm() #자료를 다 전달받지 않으면 입력 화면을 보여주도록 한다
    
    return render(request, 'registration/register.html',{'form':user_form})
