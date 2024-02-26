from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class ListaAtividades(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(null = True, blank = True)
    data_agendada = models.DateField(verbose_name = 'Data do evento')
    data_registro_agenda = models.DateTimeField(auto_now = True, verbose_name = 'Data de criação da tarefa')
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Lista_tarefas'
    
    # Referenciar o objeto pelo título na aplicação
    def __str__(self) -> str:
        return self.titulo
    
    def format_data(self):
        return self.data_agendada.strftime('%d/%m/%y')
    
    def input_data_editada(self):
        return self.data_agendada.strftime('%Y-%m-%d')
    
    def dia_tarefa(self):
        if self.data_agendada == date.today():
            return True