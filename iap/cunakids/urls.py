from django.urls import path
from . import views

app_name = 'cunakids'  # Namespace para las URLs de esta aplicación

urlpatterns = [
    path('', views.index, name='index'),  # URL para la página principal de academia

    # ... puedes agregar más URLs aquí ...
]