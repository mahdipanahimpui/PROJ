from django import forms
from . models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):

    pass1 = forms.CharField(label='password', widget=forms.PasswordInput)
    pass2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number', 'password']


    def clean_pass2(self):

        cd = self.cleaned_data
        pass1 = cd['pass1']
        pass2 = cd['pass2']

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('password must match!')
        return pass2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['pass1'])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField(
        help_text = 'you can change password using <a href="../password/">this form</a>.'
        )
    
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email', 'password', 'last_login']
    



class UserRegistrationForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)
