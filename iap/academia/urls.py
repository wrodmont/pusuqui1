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

    # URLs para Subject
    path('subjects/', views.SubjectListView.as_view(), name='subject-list'),
    path('subjects/new/', views.SubjectCreateView.as_view(), name='subject-create'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('subjects/<int:pk>/edit/', views.SubjectUpdateView.as_view(), name='subject-update'),
    path('subjects/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject-delete'),

    # URLs para Course
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/new/', views.CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),


]

 
