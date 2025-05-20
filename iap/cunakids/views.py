from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import (
    coordinator, group, server, child, assistance,
)
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import date
from .forms import (
    CoordinatorForm, GroupForm, ServerForm, ChildForm,
    AssistanceForm, # <-- Añadir AssistanceForm
)
import traceback # Para debug si es necesario

# Create your views here.

def calculated_age(born):
    if not born: return None
    today = date.today()
    age = today.year - born.year
    if (today.month, today.day) < (born.month, born.day): age -= 1
    return age

def index(request):
    """
    Vista para la página principal de la aplicación Academia.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La respuesta HTTP con el contenido de la página.
    """
    return render(request, 'cunakids/index.html')


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
    return render(request, 'cunakids/coordinator_list.html', {'coordinators': coordinators})

def coordinator_create(request):
    """
    Vista para crear un nuevo coordinador.
    """
    if request.method == 'POST':
        form = CoordinatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cunakids:coordinator_list')
    else:
        form = CoordinatorForm()
    return render(request, 'cunakids/coordinator_form.html', {'form': form, 'action': 'Crear'})

def coordinator_update(request, pk):
    """
    Vista para actualizar un coordinador existente.
    """
    coordinator_obj = get_object_or_404(coordinator, pk=pk)
    if request.method == 'POST':
        form = CoordinatorForm(request.POST, instance=coordinator_obj)
        if form.is_valid():
            form.save()
            return redirect('cunakids:coordinator_list')
    else:
        form = CoordinatorForm(instance=coordinator_obj)
    return render(request, 'cunakids/coordinator_form.html', {'form': form, 'action': 'Actualizar'})

def coordinator_delete(request, pk):
    """
    Vista para eliminar un coordinador.
    """
    coordinator_obj = get_object_or_404(coordinator, pk=pk)
    if request.method == 'POST':
        coordinator_obj.delete()
        return redirect('cunakids:coordinator_list')
    return render(request, 'cunakids/coordinator_confirm_delete.html', {'coordinator': coordinator_obj})

# vista para crear groups
def group_list(request):
    groups = group.objects.all()
    return render(request, 'cunakids/group_list.html', {'groups': groups})

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cunakids:group_list')
    else:
        form = GroupForm()
    return render(request, 'cunakids/group_form.html', {'form': form})

def group_update(request, pk):
    group_obj = get_object_or_404(group, pk=pk) 
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group_obj)
        if form.is_valid():
            form.save()
            return redirect('cunakids:group_list')
    else:
        form = GroupForm(instance=group_obj)
    return render(request, 'cunakids/group_form.html', {'form': form})

def group_delete(request, pk):
    group_obj = get_object_or_404(group, pk=pk)
    if request.method == 'POST':
        group_obj.delete()
        return redirect('cunakids:group_list')
    return render(request, 'cunakids/group_confirm_delete.html', {'group': group_obj})

class ServerListView(ListView):
    model = server
    template_name = 'cunakids/server_list.html'  # Especifica tu template
    context_object_name = 'servers'  # Nombre de la variable en el template

class ServerDetailView(DetailView):
    model = server
    template_name = 'cunakids/server_detail.html'
    context_object_name = 'server'

class ServerCreateView(CreateView):
    model = server
    form_class = ServerForm
    template_name = 'cunakids/server_form.html'
    success_url = reverse_lazy('cunakids:server_list') # Redirige a la lista después de crear

    # Opcional: Añadir contexto extra al template del formulario si es necesario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Registrar Nuevo Servidor'
        context['submit_button_text'] = 'Registrar'
        return context

class ServerUpdateView(UpdateView):
    model = server
    form_class = ServerForm
    template_name = 'cunakids/server_form.html'
    success_url = reverse_lazy('cunakids:server_list') # Redirige a la lista después de actualizar

    # Opcional: Añadir contexto extra al template del formulario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = f'Editar Servidor: {self.object.name} {self.object.surname}'
        context['submit_button_text'] = 'Actualizar'
        return context

class ServerDeleteView(DeleteView):
    model = server
    template_name = 'cunakids/server_confirm_delete.html'
    context_object_name = 'server'
    success_url = reverse_lazy('cunakids:server_list') # Redirige a la lista después de borrar

# --- Vistas para el CRUD de Kid ---

def child_list(request):
    """Vista para listar todos los niños."""
    # Obtén el queryset directamente
    children_list = child.objects.all().order_by('surname', 'name')

    # Pasa el queryset directamente al template.
    # La propiedad @property calculated_age estará disponible en cada objeto 'c' dentro del template.
    return render(request, 'cunakids/child_list.html', {'children': children_list})

def child_create(request): # <-- Renombrada
    """Vista para crear un nuevo niño."""
    if request.method == 'POST':
        form = ChildForm(request.POST) # <-- Cambiado
        if form.is_valid():
            form.save()
            return redirect('cunakids:child_list') # <-- Cambiado
    else:
        form = ChildForm() # <-- Cambiado
    # Asegúrate que el template existe o renómbralo
    return render(request, 'cunakids/child_form.html', {'form': form, 'action': 'Registrar'}) # <-- Cambiado template

def child_update(request, pk): # <-- Renombrada
    """Vista para actualizar un niño existente."""
    child_obj = get_object_or_404(child, pk=pk) # <-- Cambiado
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child_obj) # <-- Cambiado
        if form.is_valid():
            form.save()
            return redirect('cunakids:child_list') # <-- Cambiado
    else:
        form = ChildForm(instance=child_obj) # <-- Cambiado
    current_age = calculated_age(child_obj.birthday) if child_obj.birthday else "N/A"
    action_title = f"Editar Niño: {child_obj.name} {child_obj.surname} (Edad: {current_age})"
    # Asegúrate que el template existe o renómbralo
    return render(request, 'cunakids/child_form.html', {'form': form, 'action': 'Actualizar', 'action_title': action_title}) # <-- Cambiado template

def child_delete(request, pk): # <-- Renombrada
    """Vista para eliminar un niño."""
    child_obj = get_object_or_404(child, pk=pk) # <-- Cambiado
    if request.method == 'POST':
        child_obj.delete()
        return redirect('cunakids:child_list') # <-- Cambiado
    # Asegúrate que el template existe o renómbralo
    return render(request, 'cunakids/child_confirm_delete.html', {'child': child_obj}) # <-- Cambiado template y contexto


# --- Vistas para el CRUD de Assistance ---

def assistance_list(request):
    """Vista para listar todos los registros de asistencia."""
    # Optimizar consulta usando select_related para cargar datos relacionados
    assistances_list = assistance.objects.select_related(
        'child', 'date', 'group', 'coordinator'
    ).order_by('-date__date', 'child__surname', 'child__name') # Ordenar por fecha desc, luego por niño

    return render(request, 'cunakids/assistance_list.html', {'assistances': assistances_list})

def assistance_create(request):
    """Vista para crear un nuevo registro de asistencia."""
    if request.method == 'POST':
        form = AssistanceForm(request.POST)
        if form.is_valid():
            form.save()
            # Opcional: Añadir mensaje de éxito (requiere configurar messages framework)
            # messages.success(request, 'Registro de asistencia creado exitosamente.')
            return redirect('cunakids:assistance_list')
        # else:
            # Opcional: Añadir mensaje de error
            # messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = AssistanceForm()
    return render(request, 'cunakids/assistance_form.html', {'form': form, 'action': 'Registrar'})

def assistance_update(request, pk):
    """Vista para actualizar un registro de asistencia existente."""
    assistance_obj = get_object_or_404(assistance, pk=pk)
    if request.method == 'POST':
        form = AssistanceForm(request.POST, instance=assistance_obj)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Registro de asistencia actualizado.')
            return redirect('cunakids:assistance_list')
        # else:
            # messages.error(request, 'Por favor corrige los errores.')
    else:
        form = AssistanceForm(instance=assistance_obj)

    # Crear un título descriptivo
    action_title = (
        f"Editar Asistencia: {assistance_obj.child.name} {assistance_obj.child.surname} "
        f"({assistance_obj.date.date.strftime('%Y-%m-%d')})"
    )
    return render(request, 'cunakids/assistance_form.html', {
        'form': form,
        'action': 'Actualizar',
        'action_title': action_title
    })

def assistance_delete(request, pk):
    """Vista para eliminar un registro de asistencia."""
    assistance_obj = get_object_or_404(assistance.objects.select_related('child', 'date'), pk=pk)
    if request.method == 'POST':
        try:
            assistance_obj.delete()
            # messages.success(request, 'Registro de asistencia eliminado.')
            return redirect('cunakids:assistance_list')
        except Exception as e:
             # Manejar error si on_delete=PROTECT impide borrar (aunque aquí no aplica directamente)
             # messages.error(request, f'No se pudo eliminar el registro: {e}')
             # Podrías redirigir a la lista o mostrar el error en la misma página
             return render(request, 'cunakids/assistance_confirm_delete.html', {
                 'assistance': assistance_obj,
                 'error': f'Error al eliminar: {e}'
             })

    return render(request, 'cunakids/assistance_confirm_delete.html', {'assistance': assistance_obj})
