from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        content = self.request.query_params.get('content', None)
        
        if content:
            queryset = queryset.filter(content__icontains=content)
        
        return queryset

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user_id=user_id)


class Login(request):
    return render(request, 'posts/login.html')
    
class Post_details(request):
    return render(request, 'posts/post_details.html')

class Signup(request):
    return render(request, 'posts/signup.html')

class Post_list(request):
    return render(request, 'posts/post_list.html')

class Profile_update(request):
    return render(request, 'posts/profile_update.html')
