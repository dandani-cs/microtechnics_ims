from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('forgot-pass/', views.forgotpass),
    path('recover-pass/', views.newpass),
    path('home/', views.home),
    path('add', CreateUserView.as_view(), name="account_add"),
]
