from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import coordinator, group
from .forms import CoordinatorForm, GroupForm
from django.urls import reverse

# Create your views here.

def index(request):
    """
    Vista para la página principal de la aplicación Academia.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La respuesta HTTP con el contenido de la página.
    """
    return render(request, 'pusukids/index.html')


def coordinator_list(request):
    """
    Vista para listar todos los coordinadores.
    
    Args:
        request: El objeto HttpRequest.
    Returns:
    """
    print("pase por aqui")
    coordinators = coordinator.objects.all()
    print(coordinators)
    return render(request, 'pusukids/coordinator_list.html', {'coordinators': coordinators})

def coordinator_create(request):
    """
    Vista para crear un nuevo coordinador.
    """
    if request.method == 'POST':
        form = CoordinatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pusukids:coordinator_list')
    else:
        form = CoordinatorForm()
    return render(request, 'pusukids/coordinator_form.html', {'form': form, 'action': 'Crear'})

def coordinator_update(request, pk):
    """
    Vista para actualizar un coordinador existente.
    """
    coordinator_obj = get_object_or_404(coordinator, pk=pk)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, instance=coordinator_obj)
        if form.is_valid():
            form.save()
            return redirect('pusukids:coordinator_list')
    else:
        form = CoordinatorForm(instance=coordinator_obj)
    return render(request, 'pusukids/coordinator_form.html', {'form': form, 'action': 'Actualizar'})

def coordinator_delete(request, pk):
    """
    Vista para eliminar un coordinador.
    """
    coordinator_obj = get_object_or_404(coordinator, pk=pk)
    if request.method == 'POST':
        coordinator_obj.delete()
        return redirect('pusukids:coordinator_list')
    return render(request, 'pusukids/coordinator_confirm_delete.html', {'coordinator': coordinator_obj})

# vista para crear groups
def group_list(request):
    groups = group.objects.all()
    return render(request, 'pusukids/group_list.html', {'groups': groups})

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pusukids:group_list')
    else:
        form = GroupForm()
    return render(request, 'pusukids/group_form.html', {'form': form})

def group_update(request, pk):
    group = get_object_or_404(group, pk=pk) # Obtener el grupo o devolver 404
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('pusukids:group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'pusukids/group_form.html', {'form': form})

def group_delete(request, pk):
    group = get_object_or_404(group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('pusukids:group_list')
    return render(request, 'pusukids/group_confirm_delete.html', {'group': group})