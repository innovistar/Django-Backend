from django.contrib import admin

f#rom embed_video.admin import AdminVideoMixin
from .models import Course, Topic, Notification, Books, Events

# Register your models here.
#class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
#    pass

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Notification)
admin.site.register(Books)
admin.site.register(Events)
