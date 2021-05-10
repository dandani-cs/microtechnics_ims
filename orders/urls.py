from django.urls import path
from .views import CreateOrderView, ConfirmOrderView, OrderListView, OrderDetailView

urlpatterns = [
    path('', OrderListView.as_view(), name="order_view"),
    path('add', CreateOrderView.as_view(), name="order_add"),
    path('confirm', ConfirmOrderView.as_view(), name="order_confirm"),
    path('<str:pk>', OrderDetailView.as_view(), name="order_detail")
]
