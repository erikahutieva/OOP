# Generated by Django 4.1 on 2024-10-23 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0019_alter_course_name_alter_semester_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffile',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursework.subject'),
        ),
        migrations.AlterField(
            model_name='pdffile',
            name='course',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pdffile',
            name='semester',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
