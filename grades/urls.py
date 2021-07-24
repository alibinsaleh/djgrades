from django.urls import path
from grades import views


urlpatterns = [
	path('', views.home, name='home'),
	path('<int:year>/<str:month>/', views.home, name='home'),
	path('add_assignment', views.add_assignment, name='add_assignment'),

	path('all_students', views.all_students, name='all_students'),
	path('student/<int:student_id>/', views.student_details, name='student_details'),
	path('students_courses', views.students_courses, name='students_courses'),
	path('add_student', views.add_student, name='add_student'),

	path('all_courses', views.all_courses, name='all_courses'),
	path('add_course', views.add_course, name='add_course'),
	path('course/<int:course_id>/', views.course_details, name='course_details'),


]