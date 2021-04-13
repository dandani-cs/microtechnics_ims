from django.urls import path
from . import views

"""
-- first url: login.html
---- once logged in -> views.home

-- forgot pass? -> views.forgotpass -> enter email to get code
---- enter new pass & confirm new pass -> views.newpass

-- change password (user-side?)
"""

urlpatterns = [
    path('', views.login),
    path('forgot-pass/', views.forgotpass),
    path('recover-pass/', views.newpass),
    path('home/', views.home),
]
