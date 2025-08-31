from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# --- Permissions ---
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allow owners to edit/delete their own posts & comments.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return obj.author == request.user


# --- Post ViewSet ---
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# --- Comment ViewSet (no Comment.objects.all()) ---
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Restrict comments to a given post, avoids using Comment.objects.all().
        """
        post_id = self.kwargs.get("post_pk")  # comes from nested router
        return Comment.objects.filter(post__id=post_id).order_by("-created_at")

    def perform_create(self, serializer):
        """
        Attach the comment to the correct post & current user.
        """
        post_id = self.kwargs.get("post_pk")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)
