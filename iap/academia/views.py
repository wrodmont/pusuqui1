from django.shortcuts import render
# from django.http import HttpResponse # Ya no es necesaria para el index si usamos render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

from .models import Teacher
from .forms import TeacherForm

def index(request):
    """
    Vista para la página principal de la aplicación Academia.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La respuesta HTTP con el contenido de la página.
    """
    return render(request, 'academia/index.html', {'active_page': 'index'})


# Vistas para Teacher
class TeacherListView(ListView):
    model = Teacher
    template_name = 'academia/teacher_list.html' # Especificamos la plantilla
    context_object_name = 'teachers' # Nombre del objeto en el contexto de la plantilla
    paginate_by = 10 # Opcional: para paginación

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'teachers'
        context['page_title'] = 'Listado de Profesores'
        return context

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'academia/teacher_detail.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'teachers'
        context['page_title'] = f"Detalle de Profesor: {self.object.name} {self.object.surname}"
        return context

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'academia/teacher_form.html'
    success_url = reverse_lazy('academia:teacher-list') # Redirige a la lista después de crear

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'teachers'
        context['page_title'] = 'Registrar Nuevo Profesor'
        context['form_title'] = 'Formulario de Nuevo Profesor'
        context['submit_button_text'] = 'Guardar Profesor'
        return context

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'academia/teacher_form.html'
    success_url = reverse_lazy('academia:teacher-list') # Redirige a la lista después de actualizar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'teachers'
        context['page_title'] = f"Actualizar Profesor: {self.object.name} {self.object.surname}"
        context['form_title'] = 'Formulario de Actualización de Profesor'
        context['submit_button_text'] = 'Actualizar Profesor'
        return context

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'academia/teacher_confirm_delete.html'
    success_url = reverse_lazy('academia:teacher-list')
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'teachers'
        context['page_title'] = f"Eliminar Profesor: {self.object.name} {self.object.surname}"
        return context
