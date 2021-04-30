from django.urls import path
from .views import ItemListView, ItemEditListView
from . import views

urlpatterns = [
    path('view', ItemListView.as_view(), name = "view_items"),
    path('edit', ItemEditListView.as_view(), name = "edit_items"),
    path('add', views.addItem, name = "add_items"),
]
