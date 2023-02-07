# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from test_web.settings import AUTH_USER_MODEL
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, age=None, gender=None, password=None):
        if not email:
            raise ValueError('must have user email')

        user = self.model(
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            email=self.normalize_email(email), 
            age=age, 
            gender=gender, 
        )
        
        user.set_password(password) # 비밀번호 암호화
        user.save(using=self._db)
        
        print("user created")
        return user

    def create_superuser(self, username, first_name, last_name, email, age=None, gender=None, password=None):
        if not email:
            raise ValueError('must have user email')
        # if not ni:
        #     raise ValueError('must have user nickname')
        # if not name:
        #     raise ValueError('must have user name')
        user = self.model(
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            email=self.normalize_email(email), 
            age=age, 
            gender=gender, 
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        print("create superuser")
        return user

class User(AbstractUser): # Add Custom indexes by 태섭
    
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, null=True, choices=[('male','male'),('female','female'),('other','other')])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스
    objects = UserManager()

    # # 필수 작성 사항
    # REQUIRED_FIELDS = ['email', 'username']

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def save(self, *args, **kwargs):
        print("User_save : ", self.username)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.username

def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])