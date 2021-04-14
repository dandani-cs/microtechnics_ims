from django.urls import path
from .views import ItemListView

urlpatterns = [
    path('view', ItemListView.as_view(), name = "view_items")
]
