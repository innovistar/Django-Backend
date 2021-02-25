from django.db.models import Q

from django.http import HttpResponse
from django.conf import settings
#from django.core.mail import send_mail

from courses.models import Course,  Topic, Events, Books, Notification
from .serializers import CourseSerializer, TopicSerializer, EventsSerializer, NotificationSerializer, BooksSerializer

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

class CourseListView(ListAPIView):
        permission_classes = ([AllowAny])
        queryset = Course.objects.all()
        serializer_class = CourseSerializer
        
class EventsListView(ListAPIView):
        permission_classes = ([AllowAny])
        queryset = Events.objects.all()
        serializer_class = EventsSerializer
        
class BooksListView(ListAPIView):
        permission_classes = ([AllowAny])
        queryset = Books.objects.all()
        serializer_class = BooksSerializer
        
class NotificationListView(ListAPIView):
        permission_classes = ([AllowAny])
        queryset = Notification.objects.all()
        serializer_class = NotificationSerializer
        
class EventsRetrieveAPIView(RetrieveAPIView):
	permission_classes = ([AllowAny])
	queryset = Events.objects.all()
	serializer_class = EventsSerializer
	
	
class BooksRetrieveAPIView(RetrieveAPIView):
        permission_classes = ([AllowAny])
        queryset = Books.objects.all()
        serializer_class = BooksSerializer
        
class NotificationRetrieveAPIView(RetrieveAPIView):
        permission_classes = ([AllowAny])
        queryset = Notification.objects.all()
        serializer_class = NotificationSerializer


class TopicListView(ListAPIView):
	permission_classes = ([AllowAny])
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('topic', 'course__id')

	
class CourseCreateAPIView(CreateAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer                

class TopicCreateAPIView(CreateAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer

class TopicRetrieveAPIView(RetrieveAPIView):
	permission_classes = ([AllowAny])
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	#print()

class CourseRetrieveAPIView(RetrieveAPIView):
	permission_classes = ([AllowAny,])
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


@api_view(['GET', ])
@permission_classes((AllowAny, ))
def CourseTopic(request, pk):

	try:
		course = Course.objects.get(pk=pk)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	#data = {}

	title = course.title
	print("title")

	for topic in course.topic_set.all():
		print(topic)

class TopicSearchListView(ListAPIView):
	permission_classes = ([AllowAny,])
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('id','topic', 'course')

class EventsCreateAPIView(CreateAPIView):
        permission_classes = ([AllowAny])
        queryset = Events.objects.all()
        serializer_class = EventsSerializer
        
class BooksCreateAPIView(CreateAPIView):
        permission_classes = ([AllowAny])
        queryset = Books.objects.all()
        serializer_class = BooksSerializer
        
class NotificationCreateAPIView(CreateAPIView):
        permission_classes = ([AllowAny])
        queryset = Notification.objects.all()
        serializer_class = NotificationSerializer
