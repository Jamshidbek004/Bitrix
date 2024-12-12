from django.contrib import admin
from .models import Viloyat, Aperator, Royxat

@admin.register(Viloyat)
class ViloyatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Show ID and name in the admin list view
    search_fields = ('name',)     # Add a search bar for the 'name' field
    ordering = ('name',)          # Sort by name

@admin.register(Aperator)
class AperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Show ID and name in the admin list view
    search_fields = ('name',)      # Add a search bar for the 'name' field
    ordering = ('name',)           # Sort by name

@admin.register(Royxat)
class RoyxtaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ism', 'familya', 'viloyat', 'tuman', 'mahhala', 'raqam', 'kilent', 'aperator')
    search_fields = ('ism', 'familya', 'viloyat__name', 'tuman', 'mahhala', 'aperator__name')  # Searchable fields
    list_filter = ('viloyat', 'aperator')  # Add filters for 'viloyat' and 'aperator'
    ordering = ('ism', 'familya')  # Order by name and surname
    list_editable = ('tuman', 'mahhala', 'raqam', 'kilent')  # Editable fields in the list view
    list_per_page = 20  # Paginate the list view
