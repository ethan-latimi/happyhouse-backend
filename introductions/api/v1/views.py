from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from introductions.models import introduction
from introductions.serializers import IntroductionSerializer


class IntroductionList(APIView):
    def get(self, request):
        introductions = introduction.objects.all()
        serializer = IntroductionSerializer(introductions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IntroductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IntroductionDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

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
        serializer = IntroductionSerializer(intro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        intro = self.get_object(pk)
        intro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
