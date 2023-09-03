from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notices.models import Notice, Comment
from notices.serializers import NoticeSerializer, CommentSerializer
from common.permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly


class NoticeList(APIView):

    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(Notice, many=True)
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

    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def get(self, request, pk):
        comment_instance = self.get_object(pk)
        if comment_instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        comment_instance = self.get_object(pk)
        if comment_instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, comment_instance)

        serializer = CommentSerializer(comment_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment_instance = self.get_object(pk)
        if comment_instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, comment_instance)

        comment_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
