from rest_framework import viewsets
from to_do_list.models import Tarefa
from to_do_list.serializer import TarefaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
