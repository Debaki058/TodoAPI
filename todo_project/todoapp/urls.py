from django.urls import path
from todoapp import views 

urlpatterns = [
    path("student/create", views.StudentCreateAPIView.as_view(), name="create"),
    path("student/list", views.StudentListApiview.as_view(), name="list"),
    path("student/edit", views.StudentEditApiview.as_view(), name="edit"),
    path("student/delete", views.StudentDeleteApiview.as_view(), name="delete")
  
]