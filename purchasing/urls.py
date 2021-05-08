from django.urls import path
from .views import (CreatePurchasingView,
                    PurchasingListView,
                    PurchasingDetailView,
                    ConfirmPurchasingView,
                    PurchasingCancelView)

urlpatterns = [
    path('', PurchasingListView.as_view(), name="purchasing_view"),
    path('add', CreatePurchasingView.as_view(), name="purchasing_add"),
    path('confirm', ConfirmPurchasingView.as_view(), name="purchasing_confirm"),
    path('cancel/<str:purchase_num>', PurchasingCancelView.as_view(), name="purchasing_cancel_confirm"),
    path('<str:pk>', PurchasingDetailView.as_view(), name="purchasing_detail"),
]
