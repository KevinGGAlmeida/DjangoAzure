from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria,Tarefas
from .serializers import CategoriaSerializer,TarefasSerializer

# Create your views here.


class CategoriaSerializer(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()



class TarefaSerializer(viewsets.ModelViewSet):
    serializer_class = TarefasSerializer
    queryset = Tarefas.objects.all()

