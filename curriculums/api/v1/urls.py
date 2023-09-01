from django.urls import path
from .views import CurriculumList, CurriculumDetail

urlpatterns = [
    path('', CurriculumList.as_view()),
    path('<int:pk>/', CurriculumDetail.as_view()),
]
