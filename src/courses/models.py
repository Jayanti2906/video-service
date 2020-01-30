from django.db import models
from memberships.models import Membership

from django.urls import reverse

class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)
    imageslot = models.ImageField(default='')
    


    #A __str__() is a special method 
    # which tells Python how to display an object in human readable form. 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:detail',kwargs ={'slug':self.slug})
    #for making it a property we apply @property
    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

class HighlightedCourse(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
    



class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:lesson-detail',kwargs ={
            'course_slug':self.course.slug,
            'lesson_slug':self.slug,
            })
