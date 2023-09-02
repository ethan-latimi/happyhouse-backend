from django.urls import path
from .views import NoticeList, NoticeDetail

urlpatterns = [
    path('', NoticeList.as_view(), name='notice-list'),
    path('<int:pk>/', NoticeDetail.as_view(), name='notice-detail'),
]
