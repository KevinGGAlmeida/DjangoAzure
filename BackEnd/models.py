from django.db import models


# Create your models here.


class Tarefas(models.Model):
    NomeTarefa = models.TextField(max_length=100,null=False,blank=False)
    DescricaoTarefa = models.TextField(null=False,blank=False)
    DataInicio = models.DateField(auto_now_add=True,blank=True)
    Status = models.ForeignKey("Categoria",on_delete=models.CASCADE)

    def __str__(self):
        self.NomeTarefa

class Categoria(models.Model):
    
    Status = models.TextField(max_length=40)

    def __str__(self):
        return self.Status