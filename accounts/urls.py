from django.urls import path
from . import views

urlpatterns = [
    path('forgot-pass/', views.forgotpass, name="forgot_pass"),
    path('recover-pass/', views.newpass, name="recover_pass"),
    path('userManagement/', views.CreateUserView.as_view(), name="account_add"),
    
]
