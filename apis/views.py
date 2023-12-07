from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer
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

