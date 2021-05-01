from django.urls import path
from . import views

urlpatterns = [
    path('forgot-pass/', views.forgotpass, name="forgot_pass"),
    path('recover-pass/', views.newpass, name="recover_pass"),
    path('userManagement/', views.usermanagement.as_view(), name="show_list"),
    path('editUser/', views.editUser, name="edit_user"),
    path('deleteUser/<int:id>', views.deleteUser, name="delete_user")
]
