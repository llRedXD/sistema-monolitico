from django.contrib import admin
from .models import TesteUser,TesteEmpresa


class TesteUsers(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    list_per_page = 10

admin.site.register(TesteUser,TesteUsers)


class TesteEmpresas(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name',)
    list_per_page = 10

admin.site.register(TesteEmpresa, TesteEmpresas)