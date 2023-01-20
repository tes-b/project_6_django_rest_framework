from django.db import models

# Create your models here.

#user_register_dttm=> 날짜 시간 데이터 저장해주는 auto_now_add있음

class Board(models.Model):
    post_number = models.AutoField(primary_key=True)
    id = models.ForeignKey('Users', models.DO_NOTHING, db_column='id')
    contents = models.CharField(max_length=1000, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Users'

class Users(models.Model):
    member_number = models.AutoField(primary_key=True)
    id = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    latest_login = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'    