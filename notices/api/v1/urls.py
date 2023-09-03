from django.urls import path
from .views import NoticeList, NoticeDetail, CommentList, CommentDetail

urlpatterns = [
    path('', NoticeList.as_view()),
    path('<int:pk>/', NoticeDetail.as_view()),
    path('<int:notice_id>/comments/', CommentList.as_view(), name='comment-list'),
    path('<int:notice_id>/comments/<int:pk>/',
         CommentDetail.as_view(), name='comment-detail'),
]
