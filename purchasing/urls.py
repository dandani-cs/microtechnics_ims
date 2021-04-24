from django.urls import path
from .views import CreatePurchasingView, ConfirmPurchasingView

urlpatterns = [
    path('add', CreatePurchasingView.as_view(), name="purchasing_add"),
    path('confirm', ConfirmPurchasingView.as_view(), name="purchasing_add")
]
