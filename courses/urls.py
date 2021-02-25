from django.urls import path
from . import views

urlpatterns = [
    path('', views.course, name="course"),
    path('<id>/', views.course_details),
    path('create/course/', views.createCourse),
    path('user/list/', views.userCourse),
    path('user/<id>/', views.userCourseDetails),
]

