from django.db import models

# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	dob = models.DateField()

	def __str__(self):
		return self.first_name + " " + self.middle_name + " " + self.last_name