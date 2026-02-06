from django.urls import path
from .views import ResumeUploadAPI

urlpatterns = [
    path("upload/", ResumeUploadAPI.as_view()),
]
