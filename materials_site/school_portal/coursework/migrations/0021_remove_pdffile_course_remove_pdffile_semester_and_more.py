# Generated by Django 4.1 on 2024-10-23 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursework', '0020_pdffile_subject_alter_pdffile_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdffile',
            name='course',
        ),
        migrations.RemoveField(
            model_name='pdffile',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='pdffile',
            name='subject',
        ),
    ]
