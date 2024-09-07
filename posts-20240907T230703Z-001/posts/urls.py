from django.urls import path
from .views import PostListCreateView, CommentListCreateView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
