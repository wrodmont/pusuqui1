from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Sum
from .models import Assistance, Attendance, Coordinator, Group, Server, Ministry
from .forms import AssistanceForm, AttendanceForm, BatchAssistanceForm, CoordinatorForm, GroupForm,ServerForm, MinistryForm

# Create your views here.

def index(request):
    # --- General Counts ---
    total_servers = Server.objects.count()
    total_groups = Group.objects.count()
    total_coordinators = Coordinator.objects.count()

    # --- Group Attendance Stats (for the most recent date with records) ---
    latest_attendance = Attendance.objects.order_by('-date').first()
    group_stats = {}
    if latest_attendance:
        latest_date = latest_attendance.date
        # Aggregate stats for that specific date
        stats = Attendance.objects.filter(date=latest_date).aggregate(
            total_adults=Sum('adults'),
            total_youngs=Sum('youngs'),
            total_children=Sum('children')
        )
        group_stats = {
            'date': latest_date,
            'total_attendees': (stats.get('total_adults') or 0) + (stats.get('total_youngs') or 0) + (stats.get('total_children') or 0),
            'groups_attended': Attendance.objects.filter(date=latest_date, attended=True).count(),
            'total_groups_in_report': Attendance.objects.filter(date=latest_date).count()
        }

    # --- Server Assistance Stats (for the most recent date and service with records) ---
    latest_assistance = Assistance.objects.order_by('-date', '-service').first()
    server_stats = {}
    if latest_assistance:
        latest_date = latest_assistance.date
        latest_service = latest_assistance.service
        
        # Get all records for that specific date and service
        latest_service_records = Assistance.objects.filter(date=latest_date, service=latest_service)
        
        server_stats = {
            'date': latest_date,
            'service': latest_assistance.get_service_display(),
            'servers_attended': latest_service_records.filter(attended=True).count(),
            'total_servers_in_report': latest_service_records.count()
        }

    context = {
        'total_servers': total_servers,
        'total_groups': total_groups,
        'total_coordinators': total_coordinators,
        'group_stats': group_stats,
        'server_stats': server_stats,
    }
    return render(request, 'anfitriones/index.html', context)

# Views para CRUD de Coordinator
class CoordinatorListView(ListView):
    model = Coordinator
    template_name = 'anfitriones/coordinator_list.html'
    context_object_name = 'coordinators'

class CoordinatorCreateView(CreateView):
    model = Coordinator
    form_class = CoordinatorForm
    template_name = 'anfitriones/coordinator_form.html'
    success_url = reverse_lazy('anfitriones:coordinator_list')

class CoordinatorUpdateView(UpdateView):
    model = Coordinator
    form_class = CoordinatorForm
    template_name = 'anfitriones/coordinator_form.html'
    success_url = reverse_lazy('anfitriones:coordinator_list')

class CoordinatorDeleteView(DeleteView):
    model = Coordinator
    template_name = 'anfitriones/coordinator_confirm_delete.html'
    success_url = reverse_lazy('anfitriones:coordinator_list')

# Views para CRUD de Group
class GroupListView(ListView):
    model = Group
    template_name = 'anfitriones/group_list.html'
    context_object_name = 'groups'

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'anfitriones/group_form.html'
    success_url = reverse_lazy('anfitriones:group_list')

class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'anfitriones/group_form.html'
    success_url = reverse_lazy('anfitriones:group_list')

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'anfitriones/group_confirm_delete.html'
    success_url = reverse_lazy('anfitriones:group_list')  

# Vista para el CRUD de Server
class ServerListView(ListView):
    model = Server
    template_name = 'anfitriones/server_list.html'
    context_object_name = 'servers'

class ServerCreateView(CreateView):
    model = Server
    form_class = ServerForm
    template_name = 'anfitriones/server_form.html'
    success_url = reverse_lazy('anfitriones:server_list')

class ServerUpdateView(UpdateView):
    model = Server
    form_class = ServerForm
    template_name = 'anfitriones/server_form.html'
    success_url = reverse_lazy('anfitriones:server_list')

class ServerDeleteView(DeleteView):
    model = Server
    template_name = 'anfitriones/server_confirm_delete.html'
    success_url = reverse_lazy('anfitriones:server_list')

# Views para CRUD de Ministry
class MinistryListView(ListView):
    model = Ministry
    template_name = 'anfitriones/ministry_list.html'
    context_object_name = 'ministries'

class MinistryCreateView(CreateView):
    model = Ministry
    form_class = MinistryForm
    template_name = 'anfitriones/ministry_form.html'
    success_url = reverse_lazy('anfitriones:ministry_list')

class MinistryUpdateView(UpdateView):
    model = Ministry
    form_class = MinistryForm
    template_name = 'anfitriones/ministry_form.html'
    success_url = reverse_lazy('anfitriones:ministry_list')

class MinistryDeleteView(DeleteView):
    model = Ministry
    template_name = 'anfitriones/ministry_confirm_delete.html'
    success_url = reverse_lazy('anfitriones:ministry_list')

# Views para CRUD de Assistance
class AssistanceListView(ListView):
    model = Assistance
    template_name = 'anfitriones/assistance_list.html'
    context_object_name = 'assistances'

class AssistanceCreateView(CreateView):
    model = Assistance
    form_class = AssistanceForm
    template_name = 'anfitriones/assistance_form.html'
    success_url = reverse_lazy('anfitriones:assistance_list')

class AssistanceUpdateView(UpdateView):
    model = Assistance
    form_class = AssistanceForm
    template_name = 'anfitriones/assistance_form.html'
    success_url = reverse_lazy('anfitriones:assistance_list')

class AssistanceDeleteView(DeleteView):
    model = Assistance
    template_name = 'anfitriones/assistance_confirm_delete.html'
    success_url = reverse_lazy('anfitriones:assistance_list')

def batch_assistance_create(request):
    """
    Vista para crear o actualizar registros de asistencia en lote.
    """
    if request.method == 'POST':
        form = BatchAssistanceForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            starthour = form.cleaned_data['starthour']
            service = form.cleaned_data['service']

            # Iteramos sobre todos los servidores para crear/actualizar su asistencia
            for server in Server.objects.all():
                field_name = f'server_{server.pk}'
                attended = form.cleaned_data.get(field_name, False)

                # Usamos update_or_create para evitar duplicados y permitir la corrección
                Assistance.objects.update_or_create(
                    server=server,
                    date=date,
                    service=service,
                    defaults={'attended': attended, 'starthour': starthour}
                )
            return redirect('anfitriones:assistance_list')
    else:
        form = BatchAssistanceForm()

    return render(request, 'anfitriones/batch_assistance_form.html', {'form': form})

# Views para CRUD de Attendance (Estadísticas de Grupo)
class AttendanceListView(ListView):
    model = Attendance
    template_name = 'anfitriones/attendance_list.html'
    context_object_name = 'attendances'

class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'anfitriones/attendance_form.html'
    success_url = reverse_lazy('anfitriones:attendance_list')

class AttendanceUpdateView(UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'anfitriones/attendance_form.html'
    success_url = reverse_lazy('anfitriones:attendance_list')

class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = 'anfitriones/attendance_confirm_delete.html'
    success_url = reverse_lazy('anfitriones:attendance_list')