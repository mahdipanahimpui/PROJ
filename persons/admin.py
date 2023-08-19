from django.contrib import admin
from . models import Person, Field, Teacher, Participant, Education

admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Participant)
admin.site.register(Education)
admin.site.register(Field)
