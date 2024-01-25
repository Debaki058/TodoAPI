import logging
import json

from rest_framework.decorators import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated

from .models import Student
from  todoapp import global_msg
from .serializers import StudentSerializer


logger=logging.getLogger('django')  

class StudentCreateAPIView(APIView):
    authentication_classes = []  # Add appropriate authentication classes
    permission_classes = []  # Add appropriate permission classes

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

   
class StudentListApiview(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    
    def get(self,request):
        print(request.headers)
        try: 
            student=Student.objects.filter(is_delete=False)#model instance
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
    
class StudentEditApiview(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    
    
    def put(self,request,pk):
        print("edit vieww blah blah ")
        if not request.body:
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.SUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY:"success"
            }
            return JsonResponse(msg, status = status.HTTP_200_OK)
        try: 
            student=Student.objects.get(id=pk, is_delete=False)
            print(student, "hello manadhar")
            serializer = StudentSerializer(student, data=request.data)
            user=User.objects.get(username="kamal")
            if serializer.is_valid():
                serializer.save()
                msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"data update sucessfully "
                }
                return JsonResponse(msg, status = status.HTTP_400_BAD_REQUEST)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data",
                global_msg.ERROR_KEY:serializer.errors
        }
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"Not Data Found"
            }   
        except Exception as exe:
            logger.error(str(exe))
            
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
        }
        return JsonResponse(msg,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    
class StudentDeleteApiview(APIView):
    
    def delete(self,request,pk):
        
        try:
            student=Student.objects.get(id=pk)
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
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
            }
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
