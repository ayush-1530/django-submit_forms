from django.urls import path
from .import views 
from .views import student_form_view
from .views import employee_form_view


urlpatterns = [
    path('student-form/', views.student_form_view, name='student_form'),
    path('employee-form/', views.employee_form_view, name = 'employee_form')


]



