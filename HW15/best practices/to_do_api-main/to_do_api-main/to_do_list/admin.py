from django.contrib import admin
from .models import Tarefa


class Tarefas(admin.ModelAdmin):
    list_display = ("id", "titulo", "data_de_conclusao", "concluida")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo", )
    list_editable = ('concluida', )
    list_filter = ('concluida',)
    list_per_page = 10


admin.site.register(Tarefa, Tarefas)
