from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    address = models.CharField(max_length=100)
    age=models.BigIntegerField()
    mobile_number=models.BigIntegerField() 
    roll_number=models.BigIntegerField()


    class Meta:
        db_table = "student"
        
      
