# Generated by Django 3.2.4 on 2021-07-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0004_remove_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='grades.Course'),
        ),
    ]