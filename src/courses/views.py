from django.shortcuts import render
from django.views.generic import ListView,DetailView, View,CreateView
from .models import Course, Lesson, HighlightedCourse
from memberships.models import UserMembership
from django.db.models import Q

# def HighlightedView(request):
#     print("heyyyyyyyy")
#     obj = HighlightedCourse.objects.all().first()
#     print(obj)
#     context = {'object':obj}
#     return render(request,"courses/highlight.html",context)


    
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(title__icontains=query) | Q(description__icontains=query)

            results= Course.objects.filter(lookups).distinct()
            #print(results.title)

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'courses/base.html', context)

        else:
            return render(request, 'courses/base.html')

    else:
        return render(request, 'courses/base.html')



class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course

class HighlightedView(ListView):
   
    def get(self, request, *args, **kwargs):
        obj = HighlightedCourse.objects.all().first()
        course = obj.course
        model = Course.objects.all()
        context = {'object':obj,
        'course': course,
        'clist':model,
        
        }
        return render(request,'courses/highlight.html',context)  
    

    
class LessonDetailView(View):
    def get(self,request, course_slug, lesson_slug, *args, **kwargs):
        course_qs = Course.objects.filter(slug=course_slug)    
        if course_qs.exists():
            course = course_qs.first()
        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists(): 
            lesson = lesson_qs.first()
        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type
        course_allowed_mem_types = course.allowed_memberships.all()
        
        context ={
            'object': None 
        }
        #print(user_membership_type)
        if course_allowed_mem_types.filter(membership_type=user_membership_type).exists():
            context = {'object':lesson}
        return render(request,'courses/lesson_detail.html',context)  

