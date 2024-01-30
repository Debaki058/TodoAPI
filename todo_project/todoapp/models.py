from django.db import models
from account.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    address = models.CharField(max_length=100)
    mobile_number=models.BigIntegerField() 
    roll_number=models.BigIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at =  models.DateTimeField(null=True)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = "student"
        
      
