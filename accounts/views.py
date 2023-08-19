from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . forms import UserRegistrationForm
from . models import User

class CreateUserView(APIView):

    form_class = UserRegistrationForm
    template_name = 'accounts/user_create.html'
    # def get(self, request):
    #     # return Response({'hello': 'hello'})


    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    

    def post(self, requeset):
        form = self.form_class(requeset.POST)
        if form.is_valid():
            cd =  form.cleaned_data
            user = User.objects.create_user(
                phone_number=cd['phone_number'],
                password=cd['password']
            )
            return HttpResponse('regestered ok')
