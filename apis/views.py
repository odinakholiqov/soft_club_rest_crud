from rest_framework.generics import *

from .permissions import IsAuthorOrReadOnly
from .models import Post, Student
from .serializers import PostSerializer, PostDetailSerializer, StudentDetailSerializer, StudentListCreateSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class PostListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all().order_by("-id")
    serializer_class = StudentListCreateSerializer


class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer