from django.urls import path
from django.contrib.auth import views as auth_views
from .views import(
    PostListView,PostDetailView,
    PostCreateView,PostUpdateView,
    PostDeleteView
)
from .  import views

urlpatterns = [
    path("posts", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("register/", views.betterRegister, name="register"),
    path("profile/", views.profile, name="profile"),
    path("prof/", views.prof, name="prof"),
    # path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]