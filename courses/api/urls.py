from django.urls import path, include
from .views import (
	CourseListView, 
	TopicListView, 
	CourseCreateAPIView, 
	TopicCreateAPIView, 
	CourseRetrieveAPIView, 
	TopicRetrieveAPIView,
	CourseTopic,
	TopicSearchListView,
	BooksListView,
	EventsListView,
	NotificationListView,
	BooksCreateAPIView,
	EventsCreateAPIView,
	NotificationCreateAPIView,
	NotificationRetrieveAPIView,
	EventsRetrieveAPIView,
	BooksRetrieveAPIView
	)
#, OrderCreateAPIView, OrderDetailAPIView, ProductUpdateAPIView

urlpatterns = [
	path('books-list/', BooksListView.as_view(), name="books-list"),
    path('course-list/', CourseListView.as_view(), name="course-list"),
    path('events-list/', EventsListView.as_view(), name="events-list"),
    path('notice-list/', NotificationListView.as_view(), name="notice-list"),
    path('topic-list/', TopicListView.as_view(), name="topic-list"),
    path('course-create/', CourseCreateAPIView.as_view(), name="course-list"),
    path('topic-create/', TopicCreateAPIView.as_view(), name="topic-list"),
    path('topic/<pk>/', TopicRetrieveAPIView.as_view(), name="topic-detail"),
    path('event/<pk>/', EventsRetrieveAPIView.as_view(), name="event-detail"),
    path('book/<pk>/', BooksRetrieveAPIView.as_view(), name="book-detail"),
    path('notice/<pk>/', NotificationRetrieveAPIView.as_view(), name="notice-detail"),
    path('event-create/', EventsCreateAPIView.as_view(), name="event-create"),
    path('book-create/', BooksCreateAPIView.as_view(), name="book-create"),
    path('notice-create/', NotificationCreateAPIView.as_view(), name="notice-create"),
    path('course/<pk>/', CourseRetrieveAPIView.as_view(), name="course-detail"),
    path('course-topic/<pk>/', CourseRetrieveAPIView.as_view(), name="course-topic"),
    path('topic-search/', TopicSearchListView.as_view(), name="topic-search"),

]
