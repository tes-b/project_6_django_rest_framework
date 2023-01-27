# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from test_web.settings import AUTH_USER_MODEL

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, age=None, gender=None, password=None):
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
            email=email, 
            age=age, 
            gender=gender, 
        )
        user.set_password(password)
        user.save(using=self._db)
        print("create user")
        return user

class User(AbstractUser): # Add Custom indexes by 태섭
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, null=True, choices=[('Male','male'),('Female','female'),('Other','other')])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    # objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        return self.username