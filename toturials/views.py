from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from . models import Course, TakeCourse
from . serializers import CourseSerializer, TakeCourseSerializer
from rest_framework.response import Response
from rest_framework import status

class CourseViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    courses = Course.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.course = get_object_or_404(self.courses, pk=kwargs['pk'])


    def create(self, request):
        ser_data = CourseSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        ser_data = CourseSerializer(instance=self.courses, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = CourseSerializer(instance=self.course)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = CourseSerializer(instance=self.course, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        name = f'{Course}'
        self.course.delete()

        return Response({'message': f'{name} is removed'})
    

    def update(self, requesr, pk=None):
        pass





class TakeCourseViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    takecourses = TakeCourse.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.takecourse = get_object_or_404(self.takecourses, pk=kwargs['pk'])


    def create(self, request):
        ser_data = TakeCourseSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        ser_data = TakeCourseSerializer(instance=self.takecourses, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = TakeCourseSerializer(instance=self.takecourse)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = TakeCourseSerializer(instance=self.takecourse, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        name = f'{TakeCourse.id}'
        self.takecourse.delete()

        return Response({'message': f'{name} is removed'})
    

    def update(self, requesr, pk=None):
        pass