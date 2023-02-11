from django.contrib.auth    import authenticate, login
from django.shortcuts       import render, redirect
from django.core.exceptions import ValidationError

from rest_framework                         import status, generics, serializers
from rest_framework.response                import Response
from rest_framework.views                   import APIView
from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.serializers   import TokenObtainPairSerializer

from .serializers   import UserSerializer, SignInSerializer, SignUpSerializer
from .models        import User, update_last_login
from .exceptions    import CustomValidationError



# 회원가입
class SignUpAPIView(APIView):
    def post(self, request):
        print(request.POST)
        user_serializer = UserSerializer(data=request.POST)
        if user_serializer.is_valid():
            user_serializer.save()
        else :
            raise ValidationError(user_serializer.errors)
        return redirect('index')

    def get(self,request):
        return render(request=request, template_name='accounts/signup.html')

# API
class UserSignUpView(generics.CreateAPIView):
    """ 회원가입 뷰 - 요청을 보낸 사용자를 등록합니다. """
    # print("UserSignUpView") # PROCESS CHEK
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('index')



# 로그인
class LogInGenericAPIView(generics.GenericAPIView):
    """ 로그인 뷰 - 요청을 보낸 사용자를 인증합니다. """
    serializer_class = SignInSerializer
    
    def post(self, request):
        print("POST : ", request.data)
        serializer = self.get_serializer(data=request.data)
        print("POST SERIALIZER : ", serializer.is_valid())

        if serializer.is_valid(raise_exception=True):
            print("POST VALID : ", serializer)
            user = serializer.validated_data['user']
            access_token = serializer.validated_data['access']
            refresh_token = serializer.validated_data['refresh']
            res = Response(
                {
                    "user": user,
                    "token": {
                        "refresh": refresh_token,
                        "access": access_token,
                    },
                },
                status=status.HTTP_200_OK,
            ) 

            #쿠키데이터 저장
            res.set_cookie("user", user, httponly=True)
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)

            return res

        else:
            print("POST FAIL : ", serializer)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self,request):
    #     return render(request=request, template_name='accounts/login.html')



# 회원탈퇴
class WithdrawalAPIView(generics.DestroyAPIView):
    """ 회원을 삭제합니다. """
    
    # permission_classes = [IsAuthenticated] 
    # 권한 인증이 있어야 지울 수 있도록 하는 코드
    # 어떤식으로 권한 설정하는지 몰라서 일단 주석처리

    queryset = User.objects.all()
    serializer_class = UserSerializer



"""
Legacy code >>
"""

    # 참고를 위해 남겨둠            
    # ==============================================================
    # def post(self, request):
    #     user = authenticate(
    #         username=request.data.get("username"), password=request.data.get("password")
    #     )
    #     print(user)
    #     if user is not None:
    #         serializer = UserSerializer(user)
    #         print("serializer")
    #         token = TokenObtainPairSerializer.get_token(user)
    #         print("token ",token)
    #         refresh_token = str(token)
    #         access_token = str(token.access_token)
    #         print("token ",refresh_token)
    #         res = Response(
    #             {
    #                 "user": serializer.data,
    #                 "message": "login success",
    #                 "token": {
    #                     "access": access_token,
    #                     "refresh": refresh_token,
    #                 },
    #             },
    #             status=status.HTTP_200_OK,
    #         )

    #         #쿠키데이터 저장
    #         res.set_cookie("access", access_token, httponly=True)
    #         res.set_cookie("refresh", refresh_token, httponly=True)
    #         print("RES :", res)
    #         return res
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)




# from accounts.forms import UserForm

    # def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username = username, password = raw_password)  # 사용자 인증
#             login(request, user)  # 로그인
#             return redirect('index')
#     else:
#         form = UserForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# def signup(request):

#     if request.method == 'GET':
#         return render(request=request, template_name='accounts/signup.html')

#     elif request.method == 'POST':
#         user_serializer = UserSerializer(data=request.POST)
#         if user_serializer.is_valid():
#             user_serializer.save()
#         else :
#             raise ValidationError(user_serializer.errors)

#         return redirect('index')