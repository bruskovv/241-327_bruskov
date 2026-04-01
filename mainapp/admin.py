from django.contrib import admin
from .models import Perfume

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'is_in_stock')
    list_filter = ('brand', 'is_in_stock')
    search_fields = ('name', 'brand')