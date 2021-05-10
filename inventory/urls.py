from django.urls import path
from .views import ItemListView
from . import views

urlpatterns = [
    path('view', ItemListView.as_view(), name = "view_items"),
    path('read/<str:pk>/', views.ItemReadView.as_view(), name = "read_items"),
    path('add/', views.addItem, name = "add_items"),
    path('edit/<str:pk>/', views.editItem, name = "edit_items"),
    path('delete/<str:pk>/', views.deleteItem, name = "delete_items"),
    path('view_category/', views.CategoryListView.as_view(), name = "view_category"),
    path('add_category/', views.addCategory, name = "add_category"),
    path('read_cat/<str:pk>/', views.CategoryReadView.as_view(), name = "read_category"),
    path('edit_cat/<str:pk>/', views.editCategory, name = "edit_category"),
    path('delete_cat/<str:pk>/', views.deleteCategory, name = "delete_category"),
]
