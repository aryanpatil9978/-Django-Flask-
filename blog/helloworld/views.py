from django.shortcuts import render
from rest_framework.response import Response
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPosessor
from rest_framework import filters
from helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
# Create your views here.

class HelloWorldView(APIView):

    def get(self, request):
        return Response({"message": "Hello World!"})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated , IsPostPosessor]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'content']
    # def get_queryset(self):
    #     return Post.objects.filter(created_by=self.request.user)
