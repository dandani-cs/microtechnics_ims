from django.urls import path
from .views import (CreatePurchasingView,
                    PurchasingListView,
                    PurchasingDetailView,
                    ConfirmPurchasingView,
                    PurchasingCancelView,
                    PurchasingUpdateStatusView)

urlpatterns = [
    path('', PurchasingListView.as_view(), name="purchasing_view"),
    path('add', CreatePurchasingView.as_view(), name="purchasing_add"),
    path('confirm', ConfirmPurchasingView.as_view(), name="purchasing_confirm"),
    path('update_status/<str:purchase_num>', PurchasingUpdateStatusView.as_view(), name="purchasing_update_status"),
    path('cancel/<str:purchase_num>', PurchasingCancelView.as_view(), name="purchasing_cancel_confirm"),
    path('<str:pk>', PurchasingDetailView.as_view(), name="purchasing_detail"),
]
