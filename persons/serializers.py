from rest_framework import serializers
from .models import Person, Education, Field, Participant, Teacher




class PersonSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True) # return the __str__

    class Meta: 
        model = Person
        fields = '__all__'

        extra_kwargs = {
            'is_complete_data' : {'read_only': True},
        } 
        


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):
    person = serializers.StringRelatedField(read_only=True) # return the __str__
    education = serializers.StringRelatedField(read_only=True) # return the __str__
    # fields = serializers.StringRelatedField(read_only=True) # return the __str__

    class Meta:
        model = Participant
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    person = serializers.StringRelatedField(read_only=True) # return the __str__
    education = serializers.StringRelatedField(read_only=True) # return the __str__

    class Meta:
        model = Teacher
        fields = '__all__'