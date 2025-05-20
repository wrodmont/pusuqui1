# academia/views.py
from django.shortcuts import render

def index(request):
    """
    Vista para la página principal de la aplicación Academia.
    """
    return render(request, 'academia/index.html')  # Renderizamos academia/index.html

def cursos(request):
    """
    Vista para la página de cursos.
    """
    return render(request, 'academia/cursos.html')  # Necesitamos crear esta plantilla


