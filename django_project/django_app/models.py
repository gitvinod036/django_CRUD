from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class StudentDetails(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=50,null=False)
    stu_email=models.EmailField(max_length=50,default="student@gmail.com")
    stu_mobile=models.CharField(
        max_length=15,
        unique=True,
    )
    profile_pic=models.URLField(default="empty")