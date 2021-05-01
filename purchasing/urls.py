from django.urls import path
from .views import CreatePurchasingView, PurchasingListView

urlpatterns = [
    path('', PurchasingListView.as_view(), name="purchasing_view"),
    path('add', CreatePurchasingView.as_view(), name="purchasing_add")
]
