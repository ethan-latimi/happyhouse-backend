from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from introductions.models import introduction
from introductions.serializers import IntroductionSerializer
from common.permissions import IsOwnerOrReadOnly


class IntroductionList(APIView):

    def get(self, request):
        introductions = introduction.objects.all()
        serializer = IntroductionSerializer(introductions, many=True)
        return Response(serializer.data)

    def post(self, request):

        if not request.user.is_staff:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer = IntroductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class IntroductionDetail(APIView):
    def get_object(self, pk):
        try:
            return introduction.objects.get(pk=pk)
        except introduction.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        intro = self.get_object(pk)
        serializer = IntroductionSerializer(intro)
        return Response(serializer.data)

    def put(self, request, pk):
        intro = self.get_object(pk)

        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = IntroductionSerializer(intro, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        intro = self.get_object(pk)

        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        intro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
