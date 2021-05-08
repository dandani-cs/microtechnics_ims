from django.urls import path
from .views import ItemListView
from . import views

urlpatterns = [
    path('view', ItemListView.as_view(), name = "view_items"),
    path('read/<str:pk>/', views.ItemReadView.as_view(), name = "read_items"),
    path('add/', views.addItem, name = "add_items"),
    path('edit/<str:pk>/', views.editItem, name = "edit_items"),
    path('delete/<str:pk>/', views.deleteItem, name = "delete_items"),
    path('add_category/', views.addCategory, name = "add_category"),
]
