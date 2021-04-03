from django.contrib import admin
from client.models import Client


class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf',
                    'rg', 'celphone', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    list_per_page = 25
    ordering = ('name',)


admin.site.register(Client, Clients)
