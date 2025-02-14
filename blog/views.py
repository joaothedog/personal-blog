from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Define permissões personalizadas
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:  # Ações públicas
            permission_classes = [permissions.AllowAny]
        else:  # Ações privadas (create, update, delete)
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
