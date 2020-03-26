from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializer


class PostListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


def home(request):
    return render(request, "index.html")
