from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class StudentDetails(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=50,null=False)
    stu_email=models.EmailField(max_length=50,default="student@gmail.com")
    stu_mobile=models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message="Mobile number must be 10 digits and start with 6, 7, 8, or 9."
            )
        ],
        help_text="Enter a valid 10-digit mobile number starting with 6-9."
    )
    profile_pic=models.URLField(default="empty")