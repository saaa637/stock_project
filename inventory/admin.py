from django.contrib import admin
from .models import Category, Material, StockEntry

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(StockEntry)
