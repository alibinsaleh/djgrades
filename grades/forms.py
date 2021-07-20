from django import forms
from django.forms import ModelForm
from .models import Student
from .models import Course

# Create a student add form
class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ('first_name', 'middle_name', 'last_name', 'dob')
		labels = {
			'first_name': '',
			'middle_name': '',
			'last_name': '',
			'dob': '',
		}
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
			'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
			'dob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
		}

# Create a course add form
class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = "__all__"
		labels = {
			'name': '',
			'min_mark': '',
			'max_mark': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
			'min_mark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Min Mark'}),
			'max_mark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max Mark'}),
		}