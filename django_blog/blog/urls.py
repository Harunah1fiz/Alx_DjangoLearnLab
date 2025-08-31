from django.urls import path
from django.contrib.auth import views as auth_views
from .views import(
    PostListView,PostDetailView,
    PostCreateView,PostUpdateView,
    PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)
from .  import views

urlpatterns = [
        path("search/", views.search, name="search"),
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"),
    path("posts", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/comments/new/', views.CommentCreateView, name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path("/register", views.betterRegister, name="register"),
    path("/profile", views.profile, name="profile"),
    path("prof/", views.prof, name="prof"),
    # path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("/logout", auth_views.LogoutView.as_view(), name="logout"),

]