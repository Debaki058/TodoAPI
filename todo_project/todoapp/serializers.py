from rest_framework import serializers
from .models import Student
  
class StudentSerializer(serializers.Serializer):
    studentname=serializers.CharField(source='name',error_messages={"blank":"Name cannot be blank"})
    studentemail=serializers.EmailField(source='email',error_messages={"blank":"Email cannot be blank"})
    studentaddress=serializers.CharField(source='address',error_messages={"blank":"Address cannot be blank"})
    studentmobile_number=serializers.IntegerField(source='mobile_number',error_messages={"blank":"mobile number cannot be blank"})
    studentroll_number=serializers.IntegerField(source='roll_number',error_messages={"blank":"roll number cannot be blank"})
    reference_id=serializers.ReadOnlyField()
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    
    
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.email=validate_data.get('email',instance.email)
        instance.address=validate_data.get('address',instance.address),
        instance.mobile_number=validate_data.get('mobile_number',instance.mobile_number)
        instance.roll_number=validate_data.get('roll_number',instance.roll_number)
        instance.save()
        return instance
    
   
    
    def validate_studentmobile_number(self, mobile_number):
      
        if Student.objects.filter(mobile_number=mobile_number).exists():
            raise serializers.ValidationError("Mobile Number Already Exist!")
        return mobile_number


    def validate_studentemail(self, email):
      
        if Student.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email Already Exist!")
        return email
   


    
        

