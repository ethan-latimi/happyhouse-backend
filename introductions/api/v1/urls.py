from django.urls import path
from .views import IntroductionList, IntroductionDetail

urlpatterns = [
    path('', IntroductionList.as_view()),
    path('<int:pk>/', IntroductionDetail.as_view()),
]
