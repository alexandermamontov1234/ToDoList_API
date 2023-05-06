from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Task
from .permissions import IsOwner
from .serializers import TodoSerializer


class TaskAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = (IsAuthenticated, )
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = TaskAPIListPagination


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwner, )


class TaskAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsOwner, )
