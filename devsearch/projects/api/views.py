# from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from ..models import Project
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectSerializer

# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


@api_view(['GET', 'POST'])
def project_list(request):
    if (request.method == 'GET'):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    if (request.method == 'POST'):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # response is preferred over jsonresponse
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, id):
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if (request.method == 'GET'):
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif (request.method == 'PUT'):
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
