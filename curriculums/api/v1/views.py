from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from curriculums.models import Curriculum
from curriculums.serializers import CurriculumSerializer
from common.permissions import IsStaffOrReadOnly


class CurriculumList(APIView):

    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        curriculums = Curriculum.objects.all()
        serializer = CurriculumSerializer(curriculums, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = CurriculumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurriculumDetail(APIView):

    permission_classes = [IsStaffOrReadOnly]

    def get_object(self, pk):
        try:
            return Curriculum.objects.get(pk=pk)
        except Curriculum.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        curric = self.get_object(pk)
        serializer = CurriculumSerializer(curric)
        return Response(serializer.data)

    def put(self, request, pk):
        curric = self.get_object(pk)
        serializer = CurriculumSerializer(curric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        curric = self.get_object(pk)
        curric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
