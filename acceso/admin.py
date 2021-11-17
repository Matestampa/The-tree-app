from django.contrib import admin
from .models import User_data,User_access,Profile
# Register your models here.

admin.site.register([User_data,User_access,Profile])