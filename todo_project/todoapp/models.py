from django.db import models
from account.models import User



class Student(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    address = models.CharField(max_length=100)
    age=models.IntegerField()
    mobile_number=models.CharField(max_length=10)
    roll_number=models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at =  models.DateTimeField(null=True)
    is_delete = models.BooleanField(default=False)



    class Meta:
        db_table = 'student'


  