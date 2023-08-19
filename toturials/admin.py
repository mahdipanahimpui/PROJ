from django.contrib import admin
from . models import Course, TakeCourse

admin.site.register(Course)
admin.site.register(TakeCourse)