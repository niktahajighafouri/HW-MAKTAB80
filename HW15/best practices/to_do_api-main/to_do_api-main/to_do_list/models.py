from django.db import models
from datetime import date


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    data_de_conclusao = models.DateField(default=date.today, blank=True, null=True)
    concluida = models.BooleanField(default=False)
    descricao = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.titulo
