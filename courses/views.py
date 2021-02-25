from django.shortcuts import render, redirect
from .forms import CourseCreationForm
from django.http import HttpResponseRedirect

from .models import *

# Create your views here.
def course(request):
	courses = Course.objects.all()
	context = {'courses':courses}
	return render(request, 'courses/courses.html', context)


def course_details(request, id):
	if request.user.is_authenticated:
		course = Course.objects.get(id=id)
		context = {'course':course}
		return render(request, 'courses/courseDetail.html', context)
	else:
		return redirect('authenticate')

def userCourse(request):
        if request.user.is_authenticated:
                courses = Course.objects.filter(user = request.user)
                context = {'courses':courses}
                return render(request, 'courses/userCourses.html', context)
        else:
                return redirect('authenticate')
	
def userCourseDetails(request, id):
	if request.user.is_authenticated:
		course = Course.objects.get(id=id)
		print(course.title)
		context = {'course':course}
		return render(request, 'courses/userCourseDetail.html', context)

	elif request.POST.get("Upload"):
                c = course.title
                t = request.POST.get("topic")
                print(topic)
                video = request.POST.get("video_url")
                other = request.POST.get("other_url")
                topic = course.topic_set.create(course=c, topic=t, video_url=video, other_url=other)
                topic.save()
                return redirect('/')

                
                
	else:
		return redirect('authenticate')


def createCourse(request):
        users = request.user
        print(users)
        if request.method =="POST":
                form = CourseCreationForm(request.POST, request.FILES)
                if form.is_valid():
                        t= form.cleaned_data.get('title')
                        i = form.cleaned_data.get('image')
                        print(i)
                        n = form.cleaned_data.get('note')
                        course = Course.objects.create(user=users, title=t, image=i, note=n)
                        course.save()
                        return HttpResponseRedirect('/')
        else:
                form = CourseCreationForm()
        return render(request, 'courses/courseCreate.html', {'form':form})



        
