from django.urls import path
from .views import PhotoDetail, PhotoList

urlpatterns = [
    path('', PhotoList.as_view()),
    path('<int:pk>/', PhotoDetail.as_view()),
]
