from django.urls import path
from .views import ItemListView, ItemEditListView
from . import views

urlpatterns = [
    path('view', ItemListView.as_view(), name = "view_items"),
    path('add', views.addItem, name = "add_items"),
    path('edit/<str:pk>/', views.editItem, name = "edit_items"),
    path('delete/<str:pk>/', views.deleteItem, name = "delete_items"),
]
