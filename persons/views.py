from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from . models import Person, Education, Field, Teacher, Participant
from . serializers import PersonSerializer, EducationSerializer, FieldSerializer, ParticipantSerializer, TeacherSerializer
from accounts.models import User
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


class PersonView(APIView):

    persons = Person.objects.all()
    
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.person = get_object_or_404(self.persons, pk=kwargs['pk'])


    def get(self, request, pk=None):
        if pk is not None:
            ser_data = PersonSerializer(instance=self.person)
        else:
            ser_data = PersonSerializer(instance=self.persons, many=True)
        return Response(data=ser_data.data)
            

    def post(self, request):
        ser_data = PersonSerializer(data=request.POST)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)

    def delete(self, request, pk=None):
        self.person.delete()


    def put(self, request, pk=None):
        ser_data = PersonSerializer(data=request.POST, instance=self.person, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)



class EducationViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    edus = Education.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.edu = get_object_or_404(self.edus, pk=kwargs['pk'])


    def create(self, request):
        ser_data = EducationSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        ser_data = EducationSerializer(instance=self.edus, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = EducationSerializer(instance=self.edu)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = EducationSerializer(instance=self.edu, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        edu_name = self.edu.education
        self.edu.delete()

        return Response({'message': f'{edu_name} is removed'})
    

    def update(self, requesr, pk=None):
        pass




class FieldViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    fields = Field.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.field = get_object_or_404(self.fields, pk=kwargs['pk'])


    def create(self, request):
        ser_data = FieldSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        ser_data = FieldSerializer(instance=self.fields, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = FieldSerializer(instance=self.field)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = FieldSerializer(instance=self.field, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        field_name = self.field.field
        self.field.delete()

        return Response({'message': f'{field_name} is removed'})
    

    def update(self, requesr, pk=None):
        pass






class ParticipantViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    participants = Participant.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.participant = get_object_or_404(self.participants, pk=kwargs['pk'])


    def create(self, request):
        ser_data = ParticipantSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        ser_data = ParticipantSerializer(instance=self.participants, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = ParticipantSerializer(instance=self.participant)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = ParticipantSerializer(instance=self.participant, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        name = f'{Participant}'
        self.participant.delete()

        return Response({'message': f'{name} is removed'})
    

    def update(self, requesr, pk=None):
        pass






class ParticipantViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    participants = Participant.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.participant = get_object_or_404(self.participants, pk=kwargs['pk'])


    def create(self, request):
        ser_data = ParticipantSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        ser_data = ParticipantSerializer(instance=self.participants, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = ParticipantSerializer(instance=self.participant)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = ParticipantSerializer(instance=self.participant, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        name = f'{Participant}'
        self.participant.delete()

        return Response({'message': f'{name} is removed'})
    

    def update(self, requesr, pk=None):
        pass





class TeacherViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    Teachers = Teacher.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.teacher = get_object_or_404(self.Teachers, pk=kwargs['pk'])


    def create(self, request):
        ser_data = TeacherSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        print(self.Teachers)
        ser_data = TeacherSerializer(instance=self.Teachers, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = TeacherSerializer(instance=self.teacher)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = TeacherSerializer(instance=self.teacher, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        name = f'{Teacher}'
        self.teacher.delete()

        return Response({'message': f'{name} is removed'})
    

    def update(self, requesr, pk=None):
        pass