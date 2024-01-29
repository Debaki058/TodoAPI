import logging

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Student
from  todoapp import global_msg
from .serializers import StudentSerializer


logger=logging.getLogger('django')  

class StudentCreateAPIView(APIView):
    authentication_classes = []  # Add appropriate authentication classes
    permission_classes = []  # Add appropriate permission classes
    '''This class create new student only'''

    def post(self, request):
        try:
            if not request.body:
                msg = {
                    global_msg.RESPONSE_CODE_KEY: global_msg.SUCCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY: "success"
                }
                return JsonResponse(msg, status=status.HTTP_200_OK)

            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                msg = {
                    global_msg.RESPONSE_CODE_KEY: global_msg.SUCCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY: "SUCCESS OF DATA"
                }
                return JsonResponse(msg, status=status.HTTP_201_CREATED)

            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "Serializer invalid Data",
                global_msg.ERROR_KEY: serializer.errors
            }
            return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)

        except Exception as exe:
            logger.error(str(exe))
            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "Invalid Data"
            }
            return JsonResponse(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   
class StudentListApiview(APIView):
    # authentication_classes=[TokenAuthentication]
    # premission_classes=[IsAuthenticated]
    '''This class shows the all the list of student'''

    def get(self,request):
        print(request.headers)
        try: 
            student=Student.objects.all()#model instance
            serializers=StudentSerializer(student,many=True)#model instance to python
            
            msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"SUCESS OF  DATA ",
                    "data":serializers.data
                }
         
            return JsonResponse(msg, status = status.HTTP_200_OK)
            
        except Exception as exe:
            logger.error(str(exe),exc_info=True)
            
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
        }
        return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
    

        

 
class StudentEditApiView(APIView): 
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated] 
    def put(self, request,pk):
        if not request.body:
            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "Invalid Request Body!"
            }
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)

        try:
            Student = Student.objects.get(id=pk, is_delete =False) #id 1 ko details
            serializers = StudentSerializer(Student, data=request.data)
            user = User.objects.get(username='devi')

            if serializers.is_valid():
                serializers.save()
                msg = {
                    global_msg.RESPONSE_CODE_KEY: global_msg.SUCCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY: "Data Update Successfully"
                }
                return JsonResponse(msg, status=status.HTTP_200_OK)

            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "Invalid Data",
                global_msg.ERROR_KEY: serializers.errors
            }
            return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "Not Data Found"
            }
        except Exception as exe:
            logger.error(str(exe))

            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "invalid  Data"
            }
        return JsonResponse(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    


class StudentDeleteApiView(APIView): 
    authentication_classes=[]
    permission_classes=[]
    '''This class delete all the  student'''
    def delete(self,request,id):
        
        try:
            print(id)
            student=Student.objects.get(id=id)
            student.is_delete = True
            student.save()
            msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"Delete sucessfully "
                }
            return JsonResponse(msg,status=status.HTTP_200_OK)
        except ObjectDoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"Not Data Found"
            }   
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :" All Invalid Data"
            }
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
          
