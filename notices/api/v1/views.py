from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from notices.models import Notice, Comment
from notices.serializers import NoticeSerializer, CommentSerializer
from common.permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly
from django.http import Http404


class NoticeList(APIView):

    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeDetail(APIView):

    permission_classes = [IsStaffOrReadOnly]

    def get_object(self, pk):
        try:
            return Notice.objects.get(pk=pk)
        except Notice.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        notice_obj = self.get_object(pk)
        serializer = NoticeSerializer(notice_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        notice_obj = self.get_object(pk)
        serializer = NoticeSerializer(notice_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notice_obj = self.get_object(pk)
        notice_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    """
    List all comments related to a notice or create a new comment.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, notice_id, format=None):
        comments = Comment.objects.filter(notice_id=notice_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, notice_id, format=None):
        data = request.data.copy()
        data['notice'] = notice_id  # Set the notice_id in the data
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    """
    Retrieve, update, or delete a specific comment related to a notice.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, notice_id, pk):
        try:
            return Comment.objects.get(notice_id=notice_id, pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, notice_id, pk, format=None):
        comment = self.get_object(notice_id, pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, notice_id, pk, format=None):
        comment = self.get_object(notice_id, pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, notice_id, pk, format=None):
        comment = self.get_object(notice_id, pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
