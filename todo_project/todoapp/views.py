
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from todoapp.models import Student
from todoapp.serializers import StudentSerializer


class StudentListAPIView(APIView):
    authentication_classes = []  # Add appropriate authentication classes
    permission_classes = []  # Add appropriate permission classes
    '''This class post/get all the  student'''
    def post(self, request):
        try:    
            if not request.body:
                msg = {                
                    'responseCode':'1',
                    'responseMsg':"data can not be blank"
                }
                return Response(msg, status=status.HTTP_200_OK)
        
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                msg = {            
                    'responseCode':'0',
                    'responseMsg':"SUCCESS OF DATA"
                }
                return Response(msg, status=status.HTTP_201_CREATED)
            msg = {          
                'responseCode':'1',
                'responseMsg':"Serializer invalid Data",
                'errors':serializer.errors
               
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            msg = {           
                'responseCode':'1',
                'responseMsg':" invalid Data",
            }

    def get(self,request):
        print(request.headers)
        try: 
            student=Student.objects.all()#model instance
            serializers=StudentSerializer(student,many=True)#model instance to python           
            msg={
                    "message":"Success",
                    "data":serializers.data
                }
         
            return Response(msg, status = status.HTTP_200_OK)
            
        except Exception as e:
            print(e)
          
            msg={
                'status': 400,
                "message":"invalid Data"
        }
        return Response(msg,status=status.HTTP_400_BAD_REQUEST)
    
   
class StudentDetailApiview(APIView):
    authentication_classes=[JWTAuthentication]
    premission_classes=[IsAuthenticated]
    '''This class edit/delete all the  student'''

    def put(self, request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):      
        try:
            print(id)
            student=Student.objects.get(id=id)
            student.is_delete = True
            student.save()
            msg={              
                'responseCode':'0',
                'responseMsg':"Delete sucessfully"

                }
            return Response(msg,status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            print(e)
            msg={      
                'responseCode':'1',
                'responseMsg':"Not Data Found"
            }
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            msg={
                
                'responseCode':'1',
                'responseMsg':"All invalid Data"
            }
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)    
    
    

