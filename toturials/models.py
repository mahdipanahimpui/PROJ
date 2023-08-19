from django.db import models
from persons.models import Teacher, Participant

class Course(models.Model):
    name = models.CharField(max_length=128)
    
    LEVEL_CHOICE = [
        ('1', 'Beginner'),
        ('2', 'Intermediate'),
        ('3', 'Upper-Intermediate'),
        ('4', 'Advance'),
        ('5', 'Mastery'),
    ]

    level = models.CharField(choices=LEVEL_CHOICE, max_length=1)
    # NOTE: complete the date with epoch later
    # start_date = 
    # end_date = 
    presenters = models.ManyToManyField(Teacher, related_name='p_courses', blank=True)
    participants = models.ManyToManyField(Participant, related_name='p_courses', blank=True)

    def __str__(self):
        return self.name



class TakeCourse(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='p_take_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='c_take_courses')
