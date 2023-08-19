from rest_framework import serializers
from .models import Course, TakeCourse




class CourseSerializer(serializers.ModelSerializer):
    

    class Meta: 
        model = Course
        fields = '__all__'




class TakeCourseSerializer(serializers.ModelSerializer):

    class Meta: 
        model = TakeCourse
        fields = '__all__'
        
