from django.contrib import admin
from .models import Video
# Register your models here.
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'password','confirm_password')
admin.site.register(Signup,SignupAdmin)
admin.site.register(Video)