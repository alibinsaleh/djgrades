from django.shortcuts import render, get_object_or_404
from .models import Student
import calendar
from calendar import HTMLCalendar
from datetime import datetime

# Create your views here.

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	# Get names of students
	students = Student.objects.all()

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

	return render(request, 'events/home.html', 
			context= {
				'year': year,
				'month': month,
				'month_number': month_number,
				'cal': cal,
				'current_year': current_year,
				'time': time,
				'students': students,
			}
		)

def student_details(request, student_id=1):
	student = get_object_or_404(Student, pk=student_id)
	#student = Student.objects.find(student_id)

	return render(request, 'students/student_details.html', 
			context= {
				'student': student,
			}
		)