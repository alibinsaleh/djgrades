from django.db import models

# Create your models here.
class Assignment(models.Model):
	name = models.CharField('Assignment Name', max_length=250)
	assignment_date = models.DateField('Assignment Date')
	assignment_due_date =models.DateField('Assignment Due Date')
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name 

	
class Course(models.Model):
	name = models.CharField('Course Name', max_length=100)
	min_mark = models.IntegerField()
	max_mark = models.IntegerField()

	def __str__(self):
		return self.name

class Student(models.Model):
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	dob = models.DateField()
	courses = models.ManyToManyField(Course, blank=True, null=True)

	def __str__(self):
		return self.first_name + " " + self.middle_name + " " + self.last_name



class Grade(models.Model):
	student_id = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
	course_id = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE)

	grade = models.FloatField()

	def __str__(self):
		return str(self.student_id) + ' > ' + str(self.course_id)
