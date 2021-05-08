from django.urls import path
from .views import (CreatePurchasingView,
                    PurchasingListView,
                    PurchasingDetailView,
                    ConfirmPurchasingView,
                    PurchasingDeleteView)

urlpatterns = [
    path('', PurchasingListView.as_view(), name="purchasing_view"),
    path('add', CreatePurchasingView.as_view(), name="purchasing_add"),
    path('confirm', ConfirmPurchasingView.as_view(), name="purchasing_confirm"),
    path('delete/<str:purchase_num>', PurchasingDeleteView.as_view(), name="purchasing_delete"),
    path('<str:pk>', PurchasingDetailView.as_view(), name="purchasing_detail"),
]
