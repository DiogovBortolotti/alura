from django.contrib import admin
from .models import Receita

# Register your models here.
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('receita_id', 'nome_receita','categoria', 'tempo_preparo')
    list_display_links =('receita_id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page =2
admin.site.register(Receita, ListandoReceitas)