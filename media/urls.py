from django.urls import path
from .views import PhotoDetail, GetUploadURL

urlpatterns = [
    path("get-url", GetUploadURL.as_view()),
    path("<int:pk>", PhotoDetail.as_view()),
]
