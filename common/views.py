from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import EmptyPage, PageNotAnInteger
# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/v1/introductions/',
        '/api/v1/curriculums/',
        '/api/v1/notices/',
        '/api/v1/reservations/',
        '/api/v1/teachers/',
        '/api/v1/users/',
        '/api/v1/photos/',
    ]
    return Response(routes)
