from django.contrib import admin
from .models import Users

# Create your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display= ('id',
        'password',
        'name',
        'age',
        'gender',
        'email'
        )
    

