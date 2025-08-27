from django.urls import path
from django.contrib.auth import views as auth_views
from .  import views

urlpatterns = [
    path("register/", views.betterRegister, name="register"),
    path("profile/", views.profile, name="profile"),
    path("prof/", views.prof, name="prof"),
    # path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/logins.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),

]