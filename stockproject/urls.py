from django.contrib import admin
from django.urls import path
from inventory import views as inv_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inv_views.dashboard, name='dashboard'),
    path('stock-entry/', inv_views.stock_entry, name='stock_entry'),
    path('report/', inv_views.stock_report, name='stock_report'),
]
