from django.urls import path
from .views import CreateOrderView, ConfirmOrderView

urlpatterns = [
    path('add', CreateOrderView.as_view(), name="order_add"),
    path('confirm', ConfirmOrderView.as_view(), name="order_confirm"),
]
