from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('forgot-pass/', views.forgotpass, name="forgot_pass"),
    path('recover-pass/', views.newpass, name="recover_pass"),
    path('home/', views.home, name="home"),
    path('add', views.CreateUserView.as_view(), name="account_add"),
]
