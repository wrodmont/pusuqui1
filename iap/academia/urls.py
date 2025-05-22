# academia/urls.py
from django.urls import path
from . import views

app_name = 'academia'  # Namespace para las URLs de esta aplicación

urlpatterns = [
    path('', views.index, name='index'),  # URL para la página principal de academia

    # URLs para Teacher
    path('teachers/', views.TeacherListView.as_view(), name='teacher-list'),
    path('teachers/new/', views.TeacherCreateView.as_view(), name='teacher-create'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('teachers/<int:pk>/edit/', views.TeacherUpdateView.as_view(), name='teacher-update'),
    path('teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher-delete'),

    # URLs para Student
    path('students/', views.StudentListView.as_view(), name='student-list'),
    path('students/new/', views.StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    path('cursos/', views.cursos, name='cursos'),  # Ruta para la página de cursos
    # ... puedes agregar otras rutas aquí ...
]

 
