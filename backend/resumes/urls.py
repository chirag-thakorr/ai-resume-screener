from django.urls import path
from .views import JDCreateAPI, MatchAPI, ResumeUploadAPI

urlpatterns = [
    path("upload/", ResumeUploadAPI.as_view()),
    path("jd/create/", JDCreateAPI.as_view()),
    path("match/<int:jd_id>/", MatchAPI.as_view()),
]
