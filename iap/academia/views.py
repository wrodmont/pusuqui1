# academia/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.forms import formset_factory
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from datetime import date

from .models import Teacher, Student, Subject, Course, Enrollment, AttendanceLog, Grade
from .forms import (
    TeacherForm, StudentForm, SubjectForm, CourseForm, EnrollmentForm, AttendanceLogForm,
    AttendanceTakingSelectionForm, StudentAttendanceForm, GradeForm,
    GradeTakingSelectionForm, StudentGradeForm
)

def index(request):
    """
    Vista para la página principal de la aplicación Academia,
    mostrando un resumen con conteo de profesores, estudiantes,
    asignaturas y cursos.
    """
    context = {
        'total_teachers': Teacher.objects.count(),
        'total_students': Student.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_courses': Course.objects.count(),
        'active_page': 'index',
    }
    return render(request, 'academia/index.html', context)

def cursos(request):
    """
    Vista para la página de cursos.
    """
    return render(request, 'academia/cursos.html')  # Crear plantilla si no existe

# Vistas para Teacher
class TeacherListView(ListView):
    model = Teacher
    template_name = 'academia/teacher_list.html'
    context_object_name = 'teachers'
    paginate_by = 10

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
    success_url = reverse_lazy('academia:teacher-list')

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
    success_url = reverse_lazy('academia:teacher-list')

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
    template_name = 'academia/student_form.html'
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
    template_name = 'academia/student_form.html'
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
    template_name = 'academia/student_confirm_delete.html'
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
    template_name = 'academia/subject_form.html'
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
    template_name = 'academia/subject_form.html'
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
    template_name = 'academia/subject_confirm_delete.html'
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
        return Course.objects.select_related('subject', 'teacher').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'courses'
        context['page_title'] = f"Detalle de Curso: {self.object}"
        return context

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'academia/course_form.html'
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
    template_name = 'academia/course_form.html'
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
    template_name = 'academia/course_confirm_delete.html'
    success_url = reverse_lazy('academia:course-list')
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'courses'
        context['page_title'] = f"Eliminar Curso: {self.object}"
        return context

# Vistas para Enrollment
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'academia/enrollment_list.html'
    context_object_name = 'enrollments'
    paginate_by = 10

    def get_queryset(self):
        queryset = Enrollment.objects.select_related(
            'student', 'course', 'course__subject', 'course__teacher'
        ).order_by('-course__academic_period', 'course__subject__name', 'student__surname')

        # Aplicar filtros desde los parámetros GET
        course_id = self.request.GET.get('course')
        period = self.request.GET.get('period')

        if course_id:
            queryset = queryset.filter(course__id=course_id)
        if period:
            queryset = queryset.filter(course__academic_period=period)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'enrollments'
        context['page_title'] = 'Listado de Inscripciones'
        # Datos para los filtros del template
        context['all_courses'] = Course.objects.select_related('subject').order_by('-academic_period', 'subject__name')
        context['academic_periods'] = Course.objects.values_list('academic_period', flat=True).distinct().order_by('-academic_period')
        context['current_course'] = self.request.GET.get('course', '')
        context['current_period'] = self.request.GET.get('period', '')
        return context

class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'academia/enrollment_detail.html'
    context_object_name = 'enrollment'

    def get_queryset(self):
        return Enrollment.objects.select_related(
            'student', 'course', 'course__subject', 'course__teacher'
        ).prefetch_related('attendance_logs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'enrollments'
        context['page_title'] = f"Detalle de Inscripción: {self.object.student} - {self.object.course.subject}"
        return context

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'academia/enrollment_form.html'
    success_url = reverse_lazy('academia:enrollment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'enrollments'
        context['page_title'] = 'Registrar Nueva Inscripción'
        context['form_title'] = 'Formulario de Nueva Inscripción'
        context['submit_button_text'] = 'Guardar Inscripción'
        return context

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'academia/enrollment_form.html'
    success_url = reverse_lazy('academia:enrollment-list')

    def get_queryset(self):
        return Enrollment.objects.select_related(
            'student', 'course', 'course__subject', 'course__teacher'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'enrollments'
        context['page_title'] = f"Actualizar Inscripción: {self.object.student} - {self.object.course.subject}"
        context['form_title'] = 'Formulario de Actualización de Inscripción'
        context['submit_button_text'] = 'Actualizar Inscripción'
        return context

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'academia/enrollment_confirm_delete.html'
    success_url = reverse_lazy('academia:enrollment-list')
    context_object_name = 'enrollment'

    def get_queryset(self):
        return Enrollment.objects.select_related(
            'student', 'course', 'course__subject'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'enrollments'
        context['page_title'] = f"Eliminar Inscripción: {self.object.student} - {self.object.course.subject}"
        return context

# Vistas para AttendanceLog
class AttendanceLogListView(ListView):
    model = AttendanceLog
    template_name = 'academia/attendancelog_list.html'
    context_object_name = 'attendancelogs'
    paginate_by = 15

    def get_queryset(self):
        queryset = AttendanceLog.objects.select_related(
            'enrollment__student',
            'enrollment__course__subject',
            'enrollment__course__teacher'
        ).order_by('-lesson_date', 'enrollment__course__subject__name', 'enrollment__student__surname', 'lesson_number')

        # Get filter parameters
        course_id = self.request.GET.get('course')
        lesson_number = self.request.GET.get('lesson_number')

        # Apply filters
        if course_id:
            queryset = queryset.filter(enrollment__course__id=course_id)
        if lesson_number:
            queryset = queryset.filter(lesson_number=lesson_number)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'attendancelogs'
        context['page_title'] = 'Listado de Registros de Asistencia'
        context['all_courses'] = Course.objects.select_related('subject').order_by('-academic_period', 'subject__name')
        context['current_course'] = self.request.GET.get('course', '')
        context['current_lesson_number'] = self.request.GET.get('lesson_number', '')
        return context

class AttendanceLogDetailView(DetailView):
    model = AttendanceLog
    template_name = 'academia/attendancelog_detail.html'
    context_object_name = 'attendancelog'

    def get_queryset(self):
        return AttendanceLog.objects.select_related(
            'enrollment__student',
            'enrollment__course__subject',
            'enrollment__course__teacher'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'attendancelogs'
        context['page_title'] = f"Detalle de Asistencia: {self.object.enrollment.student} - L{self.object.lesson_number}"
        return context

class AttendanceLogCreateView(CreateView):
    model = AttendanceLog
    form_class = AttendanceLogForm
    template_name = 'academia/attendancelog_form.html'
    success_url = reverse_lazy('academia:attendancelog-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'attendancelogs'
        context['page_title'] = 'Registrar Nueva Asistencia'
        context['form_title'] = 'Formulario de Nuevo Registro de Asistencia'
        context['submit_button_text'] = 'Guardar Registro'
        return context

class AttendanceLogUpdateView(UpdateView):
    model = AttendanceLog
    form_class = AttendanceLogForm
    template_name = 'academia/attendancelog_form.html'
    success_url = reverse_lazy('academia:attendancelog-list')

    def get_queryset(self):
        return AttendanceLog.objects.select_related(
            'enrollment__student',
            'enrollment__course__subject'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'attendancelogs'
        context['page_title'] = f"Actualizar Asistencia: {self.object.enrollment.student} - L{self.object.lesson_number}"
        context['form_title'] = 'Formulario de Actualización de Asistencia'
        context['submit_button_text'] = 'Actualizar Registro'
        return context

class AttendanceLogDeleteView(DeleteView):
    model = AttendanceLog
    template_name = 'academia/attendancelog_confirm_delete.html'
    success_url = reverse_lazy('academia:attendancelog-list')
    context_object_name = 'attendancelog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'attendancelogs'
        context['page_title'] = f"Eliminar Registro de Asistencia: {self.object.enrollment.student} - L{self.object.lesson_number}"
        return context

class TakeAttendanceView(View):
    template_name = 'academia/take_attendance_form.html'
    selection_form_class = AttendanceTakingSelectionForm
    student_form_class = StudentAttendanceForm

    def get(self, request, *args, **kwargs):
        selection_form = self.selection_form_class(request.GET or None)
        student_formset = None
        enrollments_with_forms = []
        course_obj = None

        if selection_form.is_valid() and 'course' in request.GET:
            course_id = selection_form.cleaned_data['course'].id
            course_obj = get_object_or_404(Course.objects.select_related('subject'), pk=course_id)
            lesson_date_val = selection_form.cleaned_data['lesson_date']
            lesson_number_val = selection_form.cleaned_data['lesson_number']

            enrollments = Enrollment.objects.filter(course=course_obj).select_related('student').order_by('student__surname', 'student__name')

            StudentAttendanceFormSet = formset_factory(self.student_form_class, extra=0)
            initial_data_for_formset = []
            for enrollment in enrollments:
                try:
                    log = AttendanceLog.objects.get(enrollment=enrollment, lesson_number=lesson_number_val)
                    initial_data_for_formset.append({
                        'enrollment_id': enrollment.id,
                        'is_present': log.is_present,
                        'notes': log.notes
                    })
                except AttendanceLog.DoesNotExist:
                    initial_data_for_formset.append({
                        'enrollment_id': enrollment.id,
                        'is_present': True,
                        'notes': ''
                    })
            student_formset = StudentAttendanceFormSet(initial=initial_data_for_formset, prefix='students')

            for i, enrollment in enumerate(enrollments):
                if i < len(student_formset.forms):
                    enrollments_with_forms.append((enrollment, student_formset.forms[i]))

            selection_form = self.selection_form_class(initial={
                'course': course_obj,
                'lesson_date': lesson_date_val,
                'lesson_number': lesson_number_val
            })

        context = {
            'selection_form': selection_form,
            'student_formset': student_formset,
            'enrollments_with_forms': enrollments_with_forms,
            'course': course_obj,
            'page_title': _('Take Attendance'),
            'form_title': _('Take Attendance for Course'),
            'active_page': 'attendancelogs',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        course_id = request.POST.get('course_id_hidden')
        lesson_date_str = request.POST.get('lesson_date_hidden')
        lesson_number_str = request.POST.get('lesson_number_hidden')

        if not all([course_id, lesson_date_str, lesson_number_str]):
            messages.error(request, _("Missing course, date, or lesson number for submission."))
            return redirect(reverse_lazy('academia:take-attendance'))

        try:
            course_obj = get_object_or_404(Course.objects.select_related('subject'), pk=course_id)
            lesson_date_val = date.fromisoformat(lesson_date_str)
            lesson_number_val = int(lesson_number_str)
        except (Course.DoesNotExist, ValueError, TypeError) as e:
            messages.error(request, _("Invalid course, date, or lesson number data: %(error)s") % {'error': str(e)})
            return redirect(reverse_lazy('academia:take-attendance'))

        StudentAttendanceFormSet = formset_factory(self.student_form_class, extra=0)
        student_formset = StudentAttendanceFormSet(request.POST, prefix='students')

        if student_formset.is_valid():
            processed_count = 0
            for form_data in student_formset.cleaned_data:
                enrollment_id = form_data.get('enrollment_id')
                is_present = form_data.get('is_present', False)
                notes = form_data.get('notes', '')

                if enrollment_id:
                    try:
                        enrollment = Enrollment.objects.get(pk=enrollment_id, course=course_obj)

                        if lesson_number_val > enrollment.course.subject.number_of_lessons:
                            messages.warning(request, _("Lesson number %(lesson_num)s for student %(student)s exceeds total lessons (%(total_lessons)s). Skipped.") % {
                                'lesson_num': lesson_number_val, 'student': enrollment.student, 'total_lessons': enrollment.course.subject.number_of_lessons})
                            continue

                        AttendanceLog.objects.update_or_create(
                            enrollment=enrollment,
                            lesson_number=lesson_number_val,
                            defaults={
                                'lesson_date': lesson_date_val,
                                'is_present': is_present,
                                'notes': notes
                            }
                        )
                        processed_count += 1
                    except Enrollment.DoesNotExist:
                        messages.error(request, _("Enrollment with ID %(id)s not found for this course.") % {'id': enrollment_id})
                    except Exception as e:
                        messages.error(request, _("Error processing attendance for enrollment ID %(id)s: %(error)s") % {'id': enrollment_id, 'error': str(e)})

            messages.success(request, _("%(count)d attendance records processed for course '%(course)s' on %(date)s, lesson #%(number)s.") % {
                'count': processed_count, 'course': course_obj.subject.name, 'date': lesson_date_val.strftime('%Y-%m-%d'), 'number': lesson_number_val
            })
            return redirect(reverse_lazy('academia:attendancelog-list'))
        else:
            messages.error(request, _("There were errors in the submitted attendance data. Please review."))
            return redirect(f"{reverse_lazy('academia:take-attendance')}?course={course_id}&lesson_date={lesson_date_str}&lesson_number={lesson_number_str}")

class TakeGradesView(View):
    template_name = 'academia/take_grades_form.html'
    selection_form_class = GradeTakingSelectionForm
    student_form_class = StudentGradeForm

    def get(self, request, *args, **kwargs):
        selection_form = self.selection_form_class(request.GET or None)
        student_formset = None
        enrollments_with_forms = []
        course_obj = None

        if selection_form.is_valid() and 'course' in request.GET:
            course_obj = selection_form.cleaned_data['course']
            lesson_number_val = selection_form.cleaned_data['lesson_number']
            grade_type_val = selection_form.cleaned_data['grade_type']

            enrollments = Enrollment.objects.filter(course=course_obj).select_related('student').order_by('student__surname', 'student__name')

            StudentGradeFormSet = formset_factory(self.student_form_class, extra=0)
            initial_data_for_formset = []
            for enrollment in enrollments:
                try:
                    grade_obj = Grade.objects.get(enrollment=enrollment, lesson_number=lesson_number_val, grade_type=grade_type_val)
                    initial_data_for_formset.append({
                        'enrollment_id': enrollment.id,
                        'grade': grade_obj.grade,
                    })
                except Grade.DoesNotExist:
                    initial_data_for_formset.append({
                        'enrollment_id': enrollment.id,
                        'grade': None,
                    })
            student_formset = StudentGradeFormSet(initial=initial_data_for_formset, prefix='students')

            for i, enrollment in enumerate(enrollments):
                if i < len(student_formset.forms):
                    enrollments_with_forms.append((enrollment, student_formset.forms[i]))

            selection_form = self.selection_form_class(initial={
                'course': course_obj,
                'lesson_number': lesson_number_val,
                'grade_type': grade_type_val
            })

        context = {
            'selection_form': selection_form,
            'student_formset': student_formset,
            'enrollments_with_forms': enrollments_with_forms,
            'course': course_obj,
            'page_title': _('Take Grades'),
            'form_title': _('Take Grades for Course'),
            'active_page': 'grades',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        course_id = request.POST.get('course_id_hidden')
        lesson_number_str = request.POST.get('lesson_number_hidden')
        grade_type_str = request.POST.get('grade_type_hidden')

        if not all([course_id, lesson_number_str, grade_type_str]):
            messages.error(request, _("Missing course, lesson number, or grade type for submission."))
            return redirect(reverse_lazy('academia:take-grades'))

        try:
            course_obj = get_object_or_404(Course, pk=course_id)
            lesson_number_val = int(lesson_number_str)
            grade_type_val = grade_type_str
        except (Course.DoesNotExist, ValueError, TypeError) as e:
            messages.error(request, _("Invalid course, lesson number, or grade type data: %(error)s") % {'error': str(e)})
            return redirect(reverse_lazy('academia:take-grades'))

        StudentGradeFormSet = formset_factory(self.student_form_class, extra=0)
        student_formset = StudentGradeFormSet(request.POST, prefix='students')

        if student_formset.is_valid():
            grades_updated = 0
            grades_deleted = 0
            for form_data in student_formset.cleaned_data:
                enrollment_id = form_data.get('enrollment_id')
                grade_val = form_data.get('grade')

                if not enrollment_id:
                    continue

                try:
                    enrollment = Enrollment.objects.get(pk=enrollment_id, course=course_obj)
                    
                    if grade_val is not None:
                        # Si se proporciona una nota, se crea o actualiza.
                        Grade.objects.update_or_create(
                            enrollment=enrollment, lesson_number=lesson_number_val, grade_type=grade_type_val,
                            defaults={'grade': grade_val}
                        )
                        grades_updated += 1
                    else:
                        # Si la nota está vacía, se elimina cualquier registro existente.
                        deleted_count, deletions_by_type = Grade.objects.filter(
                            enrollment=enrollment, lesson_number=lesson_number_val, grade_type=grade_type_val
                        ).delete()
                        if deleted_count > 0:
                            grades_deleted += 1

                except Enrollment.DoesNotExist:
                    messages.error(request, _("Enrollment with ID %(id)s not found for this course.") % {'id': enrollment_id})

            success_message = _("%(updated)d grades created/updated and %(deleted)d deleted for course '%(course)s', lesson #%(number)s.") % {
                'updated': grades_updated, 'deleted': grades_deleted, 'course': course_obj.subject.name, 'number': lesson_number_val}
            messages.success(request, success_message)
            return redirect(reverse_lazy('academia:grade-list'))
        else:
            messages.error(request, _("There were errors in the submitted grade data. Please review."))
            return redirect(f"{reverse_lazy('academia:take-grades')}?course={course_id}&lesson_number={lesson_number_str}&grade_type={grade_type_str}")

# CRUD views for Grade
class GradeListView(ListView):
    model = Grade
    template_name = 'academia/grade_list.html'
    context_object_name = 'grades'
    paginate_by = 10

    def get_queryset(self):
        return Grade.objects.select_related('enrollment__student', 'enrollment__course').order_by('enrollment__student__surname', 'enrollment__course__subject__name', 'lesson_number')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'grades'
        context['page_title'] = _('List of Grades')
        return context

class GradeDetailView(DetailView):
    model = Grade
    template_name = 'academia/grade_detail.html'
    context_object_name = 'grade'

    def get_queryset(self):
        return Grade.objects.select_related('enrollment__student', 'enrollment__course')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'grades'
        context['page_title'] = _('Grade Detail')
        return context

class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'academia/grade_form.html'
    success_url = reverse_lazy('academia:grade-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'grades'
        context['page_title'] = _('Create New Grade')
        context['form_title'] = _('New Grade Form')
        context['submit_button_text'] = _('Save Grade')
        return context

class GradeUpdateView(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'academia/grade_form.html'
    success_url = reverse_lazy('academia:grade-list')

    def get_queryset(self):
        return Grade.objects.select_related('enrollment__student', 'enrollment__course')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'grades'
        context['page_title'] = _('Update Grade')
        context['form_title'] = _('Update Grade Form')
        context['submit_button_text'] = _('Update Grade')
        return context

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'academia/grade_confirm_delete.html'
    success_url = reverse_lazy('academia:grade-list')
    context_object_name = 'grade'

    def get_queryset(self):
        return Grade.objects.select_related('enrollment__student', 'enrollment__course')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'grades'
        context['page_title'] = _('Delete Grade')
        return context
