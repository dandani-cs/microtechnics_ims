from django.urls import path
from .views import CreatePurchasingView

urlpatterns = [
    path('add', CreatePurchasingView.as_view(), name="purchasing_add")
]
