# Generated by Django 3.0.2 on 2020-01-22 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
        ('courses', '0003_delete_highlightedcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighlightedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('video_url', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('allowed_memberships', models.ManyToManyField(to='memberships.Membership')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
            ],
        ),
    ]
