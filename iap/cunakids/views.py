from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Vista para la página principal de la aplicación Academia.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La respuesta HTTP con el contenido de la página.
    """
    return render(request, 'cunakids/index.html')