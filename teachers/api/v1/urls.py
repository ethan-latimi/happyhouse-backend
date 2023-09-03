from django.urls import path
from .views import TeacherList, TeacherDetail

urlpatterns = [
    path('', TeacherList.as_view(), name='teacher-list'),
    path('<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
]
