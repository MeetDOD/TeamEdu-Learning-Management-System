# Generated by Django 4.1.5 on 2023-01-21 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_studentcourseenrollment_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourseenrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrolled_student', to='main.student'),
        ),
    ]
