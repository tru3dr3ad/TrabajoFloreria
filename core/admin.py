from django.contrib import admin
from .models import Flor
# Register your models here.

class FlorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'valor', 'estado']
    search_fields = ['nombre', 'valor']
    list_filter = ['estado']
    list_per_page = 15

admin.site.register(Flor, FlorAdmin)