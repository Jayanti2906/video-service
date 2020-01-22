
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from .views import CourseListView, CourseDetailView, LessonDetailView, searchposts


app_name = 'courses'

urlpatterns = [
    path('',CourseListView.as_view(),name='list'),
    path('<slug>',CourseDetailView.as_view(),name='detail'),
    path('<course_slug>/<lesson_slug>',LessonDetailView.as_view(),name='lesson-detail'),
   
]

