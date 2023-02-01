from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import User
from django.contrib.auth.hashers import make_password
import json

# Create your tests here.
class TestUser(APITestCase):
    '''
    accounts' API (signup, signin, withdraw) unit test
    '''
    def setUp(self): # 매 테스트 전에 실행됨
        print("TestUser_setUp") # PROCESS CHECK
        self.user = User(
            id=1,
            username="test_name", 
            password=make_password("1234"),
            first_name="first_name", 
            last_name="last_name", 
            email="mail@mail.com", 
            age=20, 
            gender='male',     
        )
        self.user.save()
    
    # 회원가입
    def test_signup_success(self):
        print("TestUser_test_signup_success") # PROCESS CHECK
        self.user_data = {
            "username": "test_name_0",
            "password": "1234",
            "password_check": "1234",
            "first_name": "first_name",
            "last_name": "last_name",
            "email": "mail@mail.com",
            "age": 20,
            "gender": "male",
        }
        
        self.signup_url = "/accounts/api/signup/"
        self.reponse = self.client.post(self.signup_url, data=self.user_data, format='json')
        
        # print("TestUser_test_signup_success : ", User.objects.all()) # PROCESS CHECK
        self.assertEqual(self.reponse.status_code, status.HTTP_201_CREATED)
    
    # 중복아이디 생성 오류
    def test_signup_id_check_fail(self): 
        print("TestUser_test_signup_id_check_fail") # PROCESS CHECK
        self.user_data = {
            "username":"test_name", # 중복아이디
            "password":"1234",
            "password_check":"1234",
            "first_name":"first_name", 
            "last_name":"last_name", 
            "email":"mail@mail.com", 
            "age":20, 
            "gender":'male',     
        }
        self.signup_url = "/accounts/api/signup/"
        self.reponse = self.client.post(self.signup_url, data=self.user_data, format='json')
        self.assertEqual(self.reponse.status_code, status.HTTP_400_BAD_REQUEST) 

    # 비밀번호 오류
    def test_signup_password_check_fail(self):
        print("TestUser_signup_password_check_fail") # PROCESS CHECK
        self.user_data = {
            "username":"test_name",
            "password":"1234",
            "password_check":"12345", 
            "first_name":"first_name", 
            "last_name":"last_name", 
            "email":"mail@mail.com", 
            "age":20, 
            "gender":'male',     
        }
        self.signup_url = "/accounts/api/signup/"
        self.reponse = self.client.post(self.signup_url, data=self.user_data, format='json')
        self.assertEqual(self.reponse.status_code, status.HTTP_400_BAD_REQUEST) 

    # 로그인
    def test_login_success(self):
        print("TestUser_test_login_success") # PROCESS CHECK
        self.login_url = "/accounts/api/login/"
        data = {
            "username":"test_name", 
            "password":"1234",
        } 
        response=self.client.post(self.login_url, data=data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 로그인 존재하지 않는 아이디
    def test_login_no_username(self):
        print("TestUser_test_login_no_username") # PROCESS CHECK
        self.login_url = "/accounts/api/login/"
        data = {
            "username":"test_name_not", 
            "password":"1234",
        } 
        response=self.client.post(self.login_url, data=data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 비밀번호 불일치
    def test_password_fail(self):
        print("TestUser_test_password_fail") # PROCESS CHECK
        self.login_url = "/accounts/api/login/"
        data={
            "username":"test_name", 
            "password":"12345",
        }
        response=self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'username':"{'detail': 'No active account found with the given credentials'}"})

    # 회원탈퇴
    def test_withdraw_success(self):
        print("TestUser_test_withdraw_success") # PROCESS CHECK
        self.withdraw_url = f"/accounts/api/{self.user.id}/withdraw/"

        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.delete(self.withdraw_url, format='json')
        print("TestUser_test_withdraw_success : ", User.objects.all()) # PROCESS CHECK
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    