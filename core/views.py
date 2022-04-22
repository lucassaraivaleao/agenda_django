from django.shortcuts import redirect, render
from core.models import Evento

# Redireciona a página principal para a agenda
# def index(request):
#     return redirect('/agenda/')


def lista_eventos(request):
    # evento = Evento.objects.all()
    usuario = request.user
    # apresenta os dados cadastrados por este usuario
    evento = Evento.objects.filter(usuario=usuario)
    return render(request, 'agenda.html', {'eventos': evento})
