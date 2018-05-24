from django.db import models


class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_password=models.CharField(max_length=100)
    def __str__(self):
        return  self.user_name
# Create your models here.
class UserBlog(models.Model):
    blog_title=models.CharField(max_length=200)
    blog_content=models.TextField()
    blog_pud_time=models.DateTimeField()

    def __str__(self):
        return  self.blog_title

class UserFile(models.Model):

    file_name=models.CharField(max_length=100)
    file_upload=models.FileField(upload_to='')

    def __str__(self):
        return  self.file_name