from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


'''
This model will add 'is_examiner' and 'is_examinee' 
checkbox in the user db with all existing data fields
'''
class User(AbstractUser):
    is_examiner = models.BooleanField(default=False)
    is_examinee = models.BooleanField(default=False)

    def __str__(self):
        return self.username
