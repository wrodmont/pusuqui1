from django.urls import path
from . import views

app_name = 'pusukids'  # Namespace para las URLs de esta aplicación

urlpatterns = [
    path('', views.index, name='index'),  # URL para la página principal de pusukids

    # URLs para el CRUD de Coordinator
    path('coordinators/', views.coordinator_list, name='coordinator_list'),
    path('coordinators/new/', views.coordinator_create, name='coordinator_create'),
    path('coordinators/<int:pk>/edit/', views.coordinator_update, name='coordinator_update'),
    path('coordinators/<int:pk>/delete/', views.coordinator_delete, name='coordinator_delete'),

    #urls para el CRUD de Group
    path('groups/', views.group_list, name='group_list'),
    path('groups/new/', views.group_create, name='group_create'),
    path('groups/<int:pk>/edit/', views.group_update, name='group_update'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),

    # --- URLs para Server ---
    path('servers/', views.ServerListView.as_view(), name='server_list'),
    path('servers/<int:pk>/', views.ServerDetailView.as_view(), name='server_detail'),
    path('servers/new/', views.ServerCreateView.as_view(), name='server_create'),
    path('servers/<int:pk>/edit/', views.ServerUpdateView.as_view(), name='server_update'),
    path('servers/<int:pk>/delete/', views.ServerDeleteView.as_view(), name='server_delete'),

    # Rutas para groupage
    path('groupages/', views.groupage_list, name='groupage_list'),
    path('groupages/create/', views.groupage_create, name='groupage_create'),
    path('groupages/<int:pk>/update/', views.groupage_update, name='groupage_update'),
    path('groupages/<int:pk>/delete/', views.groupage_delete, name='groupage_delete'),
]