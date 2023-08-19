from typing import Any
from django import http
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . forms import UserRegistrationForm
from . models import User
from . serializers import UserSerializer

class UserViewSet(viewsets.ViewSet): # viewsets doesnt support instance-level permissions

    # form_class = UserRegistrationForm
    # template_name = 'accounts/user_create.html'
    # # def get(self, request):
    # #     # return Response({'hello': 'hello'})


    # def get(self, request):
    #     form = self.form_class
    #     return render(request, self.template_name, {'form': form})
    

    # def post(self, requeset):
    #     form = self.form_class(requeset.POST)
    #     if form.is_valid():
    #         cd =  form.cleaned_data
    #         user = User.objects.create_user(
    #             phone_number=cd['phone_number'],
    #             password=cd['password']
    #         )
    #         return HttpResponse('regestered ok')


    users = User.objects.all()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        if kwargs.get('pk'):
            self.user_instance = get_object_or_404(self.users, pk=kwargs['pk'])


    def create(self, request):
        ser_data = UserSerializer(data=request.POST) 

        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        ser_data = UserSerializer(instance=self.users, many=True)
        return Response(data=ser_data.data)
    

    def retrieve(self, request, pk=None):
        ser_data = UserSerializer(instance=self.user_instance)

        return Response(data=ser_data.data)
    

    def partial_update(self, request, pk=None):
        # if self.user_instance != request.user:
        #     return Response({'message': {'owner pemission denied'}})
        
        ser_data = UserSerializer(instance=self.user_instance, data=request.POST, partial=True)

        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        
        return Response(data=ser_data.errors)
    

    def destroy(self, request, pk=None):
        phone_number = self.user_instance.phone_number
        self.user_instance.is_active = False
        self.user_instance.save()

        return Response({'message': f'{phone_number} is deactivated'})
    

    def update(self, requesr, pk=None):
        pass
        
