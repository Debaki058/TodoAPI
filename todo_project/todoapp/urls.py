from django.urls import path
from . import views 

urlpatterns = [
    path("student/list/", views.StudentListAPIView.as_view(), name="post-get"),
    path("student/<int:id>/detail/", views.StudentDetailApiview.as_view(), name="delete-update")
  
]