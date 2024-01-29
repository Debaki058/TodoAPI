from django.urls import path
from . import views 

urlpatterns = [
    path("student/create/", views.StudentCreateAPIView.as_view(), name="student-create"),
    path("student/list/", views.StudentListApiview.as_view(), name="student-list"),
    path("student/<pk>edit/", views.StudentEditApiView.as_view(), name="student-edit"),
    path("student/<int:id>/delete/",views.StudentDeleteApiView.as_view(), name="student-delete")
  
]