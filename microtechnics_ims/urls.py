"""microtechnics_ims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import UserLoginView, home, export_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserLoginView.as_view(), name="final_login"),
    path('', include('django.contrib.auth.urls')),
    path('home/', home, name="home"),
    path('export_csv/', export_csv, name="export-csv"),
    path('', include("accounts.urls")),
    path('accounts/', include("accounts.urls")),
    path('inventory/', include("inventory.urls")),
    path('purchasing/', include("purchasing.urls")),
    path('orders/', include("orders.urls")),
    path('projects/', include("projects.urls")),
]
