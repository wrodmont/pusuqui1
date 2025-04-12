from django.urls import path
from . import views

app_name = 'academia'  # Namespace para las URLs de esta aplicación

urlpatterns = [
    path('', views.index, name='index'),  # URL para la página principal de academia
   # path('cursos/', views.cursos, name='cursos'),  # URL para la lista de cursos
   # path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'), # URL para el detalle de un curso
   # path('profesores/', views.profesores, name='profesores'), # URL para la lista de profesores
   # path('contacto/', views.contacto, name='contacto'), # URL para la pagina de contacto
    # ... puedes agregar más URLs aquí ...
]
