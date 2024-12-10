from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# URLConf
urlpatterns = [
    path("", views.redirect_chat, name="avacado"),
    path("auth/login/", LoginView.as_view
         (template_name="loginPage.html"), name="login-user"),
    path("auth/logout/", views.redirect_logout, name="logout-user")
]
