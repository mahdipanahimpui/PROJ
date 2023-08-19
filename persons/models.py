from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Person(models.Model):
    # NOTE: use signals here
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='u_person')
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    # NOTE: use epoch later
    birthday = models.DateTimeField(blank=True, null=True)
    # pip install pillow
    # NOTE: complete later
    # image = models.ImageField(upload_to='')
    is_complete_data = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone_number



class Field(models.Model):
    field = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.field



class Education(models.Model):
    education = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.education



class Participant(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='p_participants')
    fields = models.ManyToManyField(Field, related_name='participants',blank=True)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True, blank=True, related_name='e_participants')

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name}'


class Teacher(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='p_teacher')
    experience = models.PositiveSmallIntegerField(null=True, blank=True)
    fields = models.ManyToManyField(Field, related_name='teachers', blank=True)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL ,null=True, blank=True, related_name='e_teachers')

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name}'