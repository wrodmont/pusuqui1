# academia/views.py
from django.shortcuts import render
# from django.http import HttpResponse # Ya no es necesaria para el index si usamos render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

from .models import Teacher, Student, Subject, Course
from .forms import TeacherForm, StudentForm, SubjectForm, CourseForm

def index(request):
    """
    Vista para la página principal de la aplicación Academia.

    Args:
        request: El objeto HttpRequest.

    Returns:
        HttpResponse: La respuesta HTTP con el contenido de la página.
    """
    return render(request, 'academia/index.html', {'active_page': 'index'})  # Renderizamos academia/index.html

def cursos(request):
    """
    Vista para la página de cursos.
    """
    return render(request, 'academia/cursos.html')  # Necesitamos crear esta plantilla



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

# Vistas para Student
class StudentListView(ListView):
    model = Student
    template_name = 'academia/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'students'
        context['page_title'] = 'Listado de Estudiantes'
        return context

class StudentDetailView(DetailView):
    model = Student
    template_name = 'academia/student_detail.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'students'
        context['page_title'] = f"Detalle de Estudiante: {self.object.name} {self.object.surname}"
        return context

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'academia/student_form.html' # Podemos reutilizar o crear uno específico
    success_url = reverse_lazy('academia:student-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'students'
        context['page_title'] = 'Registrar Nuevo Estudiante'
        context['form_title'] = 'Formulario de Nuevo Estudiante'
        context['submit_button_text'] = 'Guardar Estudiante'
        return context

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'academia/student_form.html' # Reutilizamos
    success_url = reverse_lazy('academia:student-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'students'
        context['page_title'] = f"Actualizar Estudiante: {self.object.name} {self.object.surname}"
        context['form_title'] = 'Formulario de Actualización de Estudiante'
        context['submit_button_text'] = 'Actualizar Estudiante'
        return context

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'academia/student_confirm_delete.html' # Podemos reutilizar o crear uno específico
    success_url = reverse_lazy('academia:student-list')
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'students'
        context['page_title'] = f"Eliminar Estudiante: {self.object.name} {self.object.surname}"
        return context

# Vistas para Subject
class SubjectListView(ListView):
    model = Subject
    template_name = 'academia/subject_list.html'
    context_object_name = 'subjects'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'subjects'
        context['page_title'] = 'Listado de Asignaturas'
        return context

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'academia/subject_detail.html'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'subjects'
        context['page_title'] = f"Detalle de Asignatura: {self.object.name}"
        return context

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'academia/subject_form.html' # Podemos reutilizar o crear uno específico
    success_url = reverse_lazy('academia:subject-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'subjects'
        context['page_title'] = 'Registrar Nueva Asignatura'
        context['form_title'] = 'Formulario de Nueva Asignatura'
        context['submit_button_text'] = 'Guardar Asignatura'
        return context

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'academia/subject_form.html' # Reutilizamos
    success_url = reverse_lazy('academia:subject-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'subjects'
        context['page_title'] = f"Actualizar Asignatura: {self.object.name}"
        context['form_title'] = 'Formulario de Actualización de Asignatura'
        context['submit_button_text'] = 'Actualizar Asignatura'
        return context

class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'academia/subject_confirm_delete.html' # Podemos reutilizar o crear uno específico
    success_url = reverse_lazy('academia:subject-list')
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'subjects'
        context['page_title'] = f"Eliminar Asignatura: {self.object.name}"
        return context

# Vistas para Course
class CourseListView(ListView):
    model = Course
    template_name = 'academia/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10

    def get_queryset(self):
        # Optimizar la consulta para incluir los datos relacionados
        return Course.objects.select_related('subject', 'teacher').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'courses'
        context['page_title'] = 'Listado de Cursos'
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'academia/course_detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        # Optimizar la consulta para incluir los datos relacionados
        return Course.objects.select_related('subject', 'teacher').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'courses'
        context['page_title'] = f"Detalle de Curso: {self.object}" # Usa el __str__ del modelo
        return context

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'academia/course_form.html' # Reutilizar un template de formulario genérico
    success_url = reverse_lazy('academia:course-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'courses'
        context['page_title'] = 'Registrar Nuevo Curso'
        context['form_title'] = 'Formulario de Nuevo Curso'
        context['submit_button_text'] = 'Guardar Curso'
        return context

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'academia/course_form.html' # Reutilizar
    success_url = reverse_lazy('academia:course-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'courses'
        context['page_title'] = f"Actualizar Curso: {self.object}"
        context['form_title'] = 'Formulario de Actualización de Curso'
        context['submit_button_text'] = 'Actualizar Curso'
        return context

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'academia/course_confirm_delete.html' # Reutilizar
    success_url = reverse_lazy('academia:course-list')
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'courses'
        context['page_title'] = f"Eliminar Curso: {self.object}"
        return context