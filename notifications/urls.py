from django.urls import path
from .views import NotificationView
from . import views

urlpatterns = [
    path('notif-inv/', NotificationView.as_view(), name = "notif_inv"),
]