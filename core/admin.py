from django.contrib import admin
from .models import Tipo, Flor
# Register your models here.

class FlorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'valor', 'tipo']
    search_fields = ['nombre', 'tipo']
    list_filter = ['tipo']
    list_per_page = 15


admin.site.register(Tipo)
admin.site.register(Flor, FlorAdmin)