# Generated by Django 3.2.4 on 2021-07-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_course_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='grades.Course'),
        ),
    ]
