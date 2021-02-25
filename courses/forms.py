from django import forms
from .models import Course


class CourseCreationForm(forms.Form):
	title = forms.CharField(max_length=100, label="title")
	image = forms.ImageField(label="image")
	note = forms.CharField(max_length=300, label="note")


















