from django.shortcuts import render, HttpResponse, redirect
from core.models import ListaAtividades
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404
from datetime import date

# Create your views here.

# Buscar tarefa pelo título e apresentar na rota definida em urls
#def filtrar_tarefa(request, titulo):
#    objeto = ListaAtividades.objects.get(titulo = titulo)
#    return HttpResponse(f'{objeto.titulo}')


# função que lista todas as tarefas do banco de dados no arquivo html
#def agenda(request):
#    tarefa = ListaAtividades.objects.all()
#    response = {'Tarefas': tarefa}
#    return render(request, 'agenda.html', response)

@login_required(login_url='/login')
# função que filtra todas as tarefas registradas por um usuario
def agenda(request):
    usuario = request.user
    data_atual = date.today()
    tarefa = ListaAtividades.objects.filter(usuario = usuario, data_agendada__gt = data_atual)
    response = {'Tarefas': tarefa}
    return render(request, 'agenda.html', response)


@login_required(login_url='/login')
def tarefa(request):
    id_tarefa = request.GET.get('id')
    dados = {}

    if id_tarefa:
        dados['tarefa'] = ListaAtividades.objects.get(id = id_tarefa)
    return render(request, 'pagina_tarefas.html', dados)


# Função para inicio da aplicação
#def inicio(request):
#    return redirect('/agenda/')

def login_usuario(request):
    return render(request, 'login.html')


def logout_usuario(request):
    logout(request)
    return redirect('/login/')


def confirmar_acesso(request):
    if request.POST:
        nome_usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome_usuario, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        
        else:
            messages.error(request, "Usuário não encontrado")

    return redirect('/')

@login_required(login_url='/login')
def registrar_tarefa(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_atividade = request.POST.get('data_atividade')
        descricao = request.POST.get('descrição')
        usuario = request.user
        id = request.POST.get('id_tarefa')

        if id:
            ListaAtividades.objects.filter(id = id).update(titulo = titulo,
                                                           data_agendada = data_atividade,
                                                           descricao = descricao,
                                                           usuario = usuario)

        else:
            ListaAtividades.objects.create(titulo = titulo,
                                        data_agendada = data_atividade,
                                        descricao = descricao,
                                        usuario = usuario)
        return redirect('/')
    
    return redirect('/')

@login_required(login_url='/login')
def deletar_tarefa(request, id_tarefa):
    try:
        usuario = request.user
        registro_tarefa = ListaAtividades.objects.get(id = id_tarefa, usuario = usuario)
        
    except Exception:
        raise Http404()

    if usuario == registro_tarefa.usuario:
        registro_tarefa.delete()
    
    else:
        raise Http404()
    
    return redirect('/')