"""
URL configuration for Agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/',views.agenda),
    path('agenda/tarefa/', views.tarefa),
    path('agenda/tarefa/submit', views.registrar_tarefa),
    path('agenda/tarefa/delete/<int:id_tarefa>/', views.deletar_tarefa),
    #path('', views.inicio)
    path('',RedirectView.as_view(url = '/agenda/')),
    path('login/', views.login_usuario),
    path('login/submit', views.confirmar_acesso),
    path('logout/', views.logout_usuario)
]
