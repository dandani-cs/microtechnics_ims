from django.urls import path
from . import views

"""
-- first url: login.html
---- once logged in -> views.home
"""

urlpatterns = [
    path('', views.login),
    path('forgot-pass/', views.forgotpass),
    path('home/', views.home),
    path('add', CreateUserView.as_view(), name="account_add"),
]
