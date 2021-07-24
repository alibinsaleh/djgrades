from django.shortcuts import render, get_object_or_404
from .models import Student
from .models import Course
from .models import Grade
from .models import Assignment
from .forms import AssignmentForm
from .forms import StudentForm
from .forms import CourseForm
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime


# Create your views here.

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	# Get names of students
	assignments_list = Assignment.objects.all().order_by('-assignment_date')

	month = month.capitalize()
	# Convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)
	# Create a calendar
	cal = HTMLCalendar().formatmonth(year, month_number)
	
	# Get current year
	now = datetime.now()
	current_year = now.year

	# Get current time
	time = now.strftime('%I:%M:%S %p')

	return render(request, 'home.html', 
			context= {
				'year': year,
				'month': month,
				'month_number': month_number,
				'cal': cal,
				'current_year': current_year,
				'time': time,
				'now': now.date(),
				'assignments_list':assignments_list,
			}
		)
# Add new Assignment
def add_assignment(request):
	submitted = False
	if request.method == 'POST':
		form = AssignmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_assignment?submitted=True')
	else:
		form = AssignmentForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'assignments/add_assignment.html', {'form': form, 'submitted': submitted})



def all_students(request):
	students_list = Student.objects.all()
	return render(request, 'students/all_students.html', {'students_list': students_list})


def student_details(request, student_id=1):
	student = get_object_or_404(Student, pk=student_id)
	#student = Student.objects.find(student_id)

	return render(request, 'students/student_details.html', 
			context= {
				'student': student,
			}
		)



def students_courses(request):
	student_list = Student.objects.all()
	grade_list = Grade.objects.all()
	return render(request, 'students/students_courses.html', {
		'student_list': student_list,
		'grade_list': grade_list
		})

def add_student(request):
	submitted = False
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_student?submitted=True')
	else:
		form = StudentForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'students/add_student.html', {'form': form, 'submitted': submitted})


# -----------  Courses views --------------
def all_courses(request):
	courses_list = Course.objects.all()
	return render(request, 'courses/all_courses.html', {'courses_list': courses_list})


def course_details(request, course_id):
	course = Course.objects.get(pk=course_id)
	return render(request, 'courses/course_details.html', {'course': course})

def add_course(request):
	submitted = False
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_course?submitted=True')
	else:
		form = CourseForm
		if 'submitted' in request.GET:
			submitted = True
	
	return render(request, 'courses/add_course.html', {'form': form, 'submitted': submitted})





