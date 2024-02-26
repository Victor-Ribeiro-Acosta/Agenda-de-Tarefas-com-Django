from django.contrib import admin
from core.models import ListaAtividades

# Register your models here.

# Classe que apresenta as informações desejadas na tela da agenda
class TelaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_agendada', 'data_registro_agenda')
    list_filter = ('usuario','data_agendada')


# Registrando as classes na aplicação
admin.site.register(ListaAtividades, TelaAdmin)