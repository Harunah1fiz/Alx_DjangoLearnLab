from django.urls import path
from .views import PostCreateView, PostListView, FeedView, index
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path('', index, name='index'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('all/', PostListView.as_view(), name='all-posts'),
    path('feed/', FeedView.as_view(), name='feed'), 
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
