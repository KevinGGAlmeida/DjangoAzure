from django.contrib import admin
from .models import Categoria,Tarefas

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display =['Status']

class TarefasAdmin(admin.ModelAdmin):
    list_display =("NomeTarefa",'DescricaoTarefa','DataInicio','Status')


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Tarefas,TarefasAdmin)