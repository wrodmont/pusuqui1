from django import forms
from .models import Teacher, Student

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