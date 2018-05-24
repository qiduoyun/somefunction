from django.contrib import admin
from .models import User,UserBlog,UserFile
admin.site.register(User)
admin.site.register(UserBlog)
admin.site.register(UserFile)
# Register your models here.
