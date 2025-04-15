from django.urls import path
from . import views

app_name = 'pusukids'  # Namespace para las URLs de esta aplicación

urlpatterns = [
    path('', views.index, name='index'),  # URL para la página principal de pusukids

    # URLs para el CRUD de Coordinator
    path('coordinator_list/', views.coordinator_list, name='coordinator_list'),
    path('coordinator_form/', views.coordinator_create, name='coordinator_create'),
    path('coordinator_form/<int:pk>/', views.coordinator_update, name='coordinator_update'),
    path('coordinator_confirm_delete/<int:pk>/', views.coordinator_delete, name='coordinator_delete'),

    #urls para el CRUD de Group
    path('group_list/', views.group_list, name='group_list'),
    path('group_form/', views.group_create, name='group_create'),
    path('group_form/<int:pk>/', views.group_update, name='group_update'),
    path('group_confirm_delete/<int:pk>/', views.group_delete, name='group_delete'),

    # --- URLs para Server ---
    path('servers/', views.ServerListView.as_view(), name='server_list'),
    path('servers/<int:pk>/', views.ServerDetailView.as_view(), name='server_detail'),
    path('servers/new/', views.ServerCreateView.as_view(), name='server_create'),
    path('servers/<int:pk>/edit/', views.ServerUpdateView.as_view(), name='server_update'),
    path('servers/<int:pk>/delete/', views.ServerDeleteView.as_view(), name='server_delete'),


]