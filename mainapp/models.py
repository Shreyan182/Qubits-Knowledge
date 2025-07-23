from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('college', 'College'),
        ('recruiter', 'Recruiter'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
# Create your models here.
