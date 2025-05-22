from django import forms
from .models import Teacher, Student, Subject, Course

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre',
            'surname': 'Apellido',
            'email': 'Correo Electrónico',
            'phone_number': 'Número de Teléfono',
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'email', 'phone_number', 'date_of_birth']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'name': 'Nombre',
            'surname': 'Apellido',
            'email': 'Correo Electrónico',
            'phone_number': 'Número de Teléfono',
            'date_of_birth': 'Fecha de Nacimiento',
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description', 'number_of_lessons']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'number_of_lessons': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre de la Asignatura',
            'description': 'Descripción',
            'number_of_lessons': 'Número de Lecciones',
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'subject', 'teacher', 'academic_period', 'day_of_week',
            'start_time', 'start_date', 'end_date', 'is_active'
        ]
        widgets = {
            'subject': forms.Select(attrs={'class': 'form-control select2'}), # Usar select2 para mejor UX
            'teacher': forms.Select(attrs={'class': 'form-control select2'}), # Usar select2 para mejor UX
            'academic_period': forms.TextInput(attrs={'class': 'form-control'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # El modelo lo calcula si se deja vacío
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'subject': 'Asignatura',
            'teacher': 'Profesor',
            'academic_period': 'Periodo Académico',
            'day_of_week': 'Día de la Semana',
            'start_time': 'Hora de Inicio',
            'start_date': 'Fecha de Inicio',
            'end_date': 'Fecha de Fin (opcional, se calcula si se deja en blanco)',
            'is_active': '¿Está Activo?',
        }
        help_texts = {
            'end_date': model._meta.get_field('end_date').help_text # Heredar help_text del modelo
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # El campo end_date no es obligatorio en el formulario ya que el modelo puede calcularlo.
        self.fields['end_date'].required = False