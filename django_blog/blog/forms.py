from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,post

class UserRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'phone_number']

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title','content']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("the title must be at least 5 characters Long.")
        return title
