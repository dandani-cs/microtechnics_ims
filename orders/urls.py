from django.urls import path
from .views import CreateOrderView, ConfirmOrderView, OrderListView, OrderDetailView, OrderUpdateStatusView, OrderCancelConfirmView

urlpatterns = [
    path('', OrderListView.as_view(), name="order_view"),
    path('add', CreateOrderView.as_view(), name="order_add"),
    path('confirm', ConfirmOrderView.as_view(), name="order_confirm"),
    path('cancel/<str:order_num>', OrderCancelConfirmView.as_view(), name="order_cancel_confirm"),
    path('update_status/<str:order_num>', OrderUpdateStatusView.as_view(), name="order_update_status"),
    path('<str:pk>', OrderDetailView.as_view(), name="order_detail")
]
