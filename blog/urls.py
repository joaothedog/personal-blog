from django.urls import path
from .views import PostViewSet

urlpatterns = [
    # Endpoints públicos
    path('posts/', PostViewSet.as_view({'get': 'list'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve'}), name='post-detail'),

    # Endpoints privados (apenas para você, autenticado)
    path('posts/create/', PostViewSet.as_view({'post': 'create'}), name='post-create'),
    path('posts/<int:pk>/update/', PostViewSet.as_view({'put': 'update'}), name='post-update'),
    path('posts/<int:pk>/delete/', PostViewSet.as_view({'delete': 'destroy'}), name='post-delete'),
]