from django.urls import path
from . import views

urlpatterns = [
    path('forgot-pass/', views.forgotpass, name="forgot_pass"),
    path('recover-pass/', views.newpass, name="recover_pass"),
    path('add/', views.CreateUserView.as_view(), name="account_add"),
    path('home/', views.home, name="home"),
    path('export_csv/', views.export_csv, name="export-csv"),
]
