from django.urls import path
from . import views

urlpatterns = [
    path('forgot-pass/', views.forgotpass, name="forgot_pass"),
    path('recover-pass/', views.newpass, name="recover_pass"),
    path('accounts_add', views.CreateUserView.as_view(), name="add_user"),
    path('user_profile/<str:employee_id>', views.userProfile, name="user_profile"),
    path('userManagement/', views.usermanagement.as_view(), name="show_list"),
    path('editUser/<str:employee_id>', views.editUser, name="edit_user"),
    path('deleteUser/<str:employee_id>', views.deleteUser, name="delete_user")
]
