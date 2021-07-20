# Generated by Django 3.2.4 on 2021-07-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0006_auto_20210719_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='grades.Course'),
        ),
        migrations.RemoveField(
            model_name='grade',
            name='course_id',
        ),
        migrations.AddField(
            model_name='grade',
            name='course_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grades.course'),
        ),
        migrations.RemoveField(
            model_name='grade',
            name='student_id',
        ),
        migrations.AddField(
            model_name='grade',
            name='student_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grades.student'),
        ),
    ]