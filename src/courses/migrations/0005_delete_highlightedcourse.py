# Generated by Django 3.0.2 on 2020-01-22 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_highlightedcourse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HighlightedCourse',
        ),
    ]