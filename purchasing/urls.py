from django.urls import path
from .views import CreatePurchasingView, PurchasingListView, PurchasingDetailView

urlpatterns = [
    path('', PurchasingListView.as_view(), name="purchasing_view"),
    path('add', CreatePurchasingView.as_view(), name="purchasing_add"),
    path('<str:pk>', PurchasingDetailView.as_view(), name="purchasing_detail")
]
