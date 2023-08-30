from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import notice, photo
from .serializers import NoticeSerializer, PhotoSerializer


class NoticeList(APIView):
    def get(self, request):
        notices = notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = NoticeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeDetail(APIView):
    def get_object(self, pk):
        try:
            return notice.objects.get(pk=pk)
        except notice.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        notice_obj = self.get_object(pk)
        serializer = NoticeSerializer(notice_obj)
        return Response(serializer.data)

    def put(self, request, pk):
        notice_obj = self.get_object(pk)
        if notice_obj.owner != request.user:
            # Unauthorized to update
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = NoticeSerializer(notice_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notice_obj = self.get_object(pk)
        if notice_obj.owner != request.user:
            # Unauthorized to delete
            return Response(status=status.HTTP_403_FORBIDDEN)
        notice_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoList(APIView):
    def get(self, request):
        photos = photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
