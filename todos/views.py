from django.shortcuts import render

from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def todosList(request):
    user = request.user
    todos = Todo.objects.filter(owner=user)
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def todoDetail(request, id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTodo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateTodo(request, id):
    todo = Todo.objects.get(id=id)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTodo(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return Response("Todo Deleted Successfully!..")