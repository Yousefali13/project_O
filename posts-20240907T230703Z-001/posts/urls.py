from django.urls import path
from .views import PostListCreateView, CommentListCreateView

urlpatterns = [
    #path('', PostListCreateView.as_view(), name='post-list-create'),
    #path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('', viwes.login, name = 'login')
    path('postdetails', viwes.post_details, name = 'post_details')
    path('postlist', viwes.post_list, name = 'post_list')
    path('signup', viwes.signup, name = 'signup')
    path('profileupdate', viwes.profile_update, name = 'profile_update')
]
