from rest_framework import serializers
from .models import Course, TakeCourse
from persons.serializers import ParticipantSerializer



class CourseSerializer(serializers.ModelSerializer):
    
    # participants = ParticipantSerializer(many=True)

    class Meta: 
        model = Course
        fields = '__all__'




class TakeCourseSerializer(serializers.ModelSerializer):

    class Meta: 
        model = TakeCourse
        fields = '__all__'
        
