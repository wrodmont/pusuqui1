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

   # path('cursos/', views.cursos, name='cursos'),  # URL para la lista de cursos
   # path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'), # URL para el detalle de un curso
   # path('profesores/', views.profesores, name='profesores'), # URL para la lista de profesores
   # path('contacto/', views.contacto, name='contacto'), # URL para la pagina de contacto
    # ... puedes agregar más URLs aquí ...
]

 
