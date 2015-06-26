from django import forms
from django.contrib.auth.models import User
from blogging.models import UserProfile,blogtext



class BlogForm(forms.ModelForm):
    text=forms.CharField(max_length=256,blank=False)
    class Meta :
        model=blogtext
        fields=('text')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')