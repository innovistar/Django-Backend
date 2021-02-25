from django.db import models

#from embed_video.fields import EmbedVideoField

#from django.contrib.auth.models import User

#from users.models import Account


# Create your models here.
class Course(models.Model):
    #user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    #course = EmbedVideoField(null=True)
    url = models.CharField(max_length=2000, null=True, blank=True)
    note = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title
        
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except :
            url = ''
        return url

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=2000)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    #video_url = EmbedVideoField(null=True)
    other_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.topic

        
        
class Notification(models.Model):
	title = models.CharField(max_length=200, null=True)
	notice = models.CharField(max_length=2000)
	
	def __str__(self):
		return self.notice
	
class Books(models.Model):
	image = models.ImageField(null=True, blank=True)
	title = models.CharField(max_length=200)
	note = models.CharField(max_length=10000, null=True, blank=True)
	image_url = models.CharField(max_length=2000, null=True, blank=True)
	url = models.CharField(max_length=200)
	
	def __str__(self):
		return self.title

	@property
    def imageURL(self):
        try:
            url = self.image.url
        except :
            url = ''
        return url
	
class Events(models.Model):
	event = models.ImageField(null=True, blank=True)
	title = models.CharField(max_length=200)
	note = models.CharField(max_length=10000, null=True, blank=True)
	url = models.CharField(max_length=200)
	image_url = models.CharField(max_length=2000, null=True, blank=True)
	#videourl = EmbedVideoField(null=True, blank=True)
	
	
	def __str__(self):
		return self.url


	@property
    def imageURL(self):
        try:
            url = self.image.url
        except :
            url = ''
        return url
	
	

	
	
	
	

	
