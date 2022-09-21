from rest_framework import serializers
from .models import Categoria,Tarefas


class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = ('id',"NomeTarefa",'DescricaoTarefa','DataInicio','Status')



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','Status')


