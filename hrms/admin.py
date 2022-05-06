from django.contrib import admin
from .models import Employee,Department,Attendance,Kin
# from django.contrib.auth.models import AbstractUser
# Register your models here.
admin.site.register([Employee,Department,Attendance,Kin])
# admin.site.register([user])

