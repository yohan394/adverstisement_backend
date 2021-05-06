from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=True,
                                 help_text='Your first name will be presented when using chat application.')
    last_name = forms.CharField(max_length=30, required=True,
                                help_text='Your last name will be presented when using chat application.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Optional. Format: YYYY-MM-DD', required=False)
    bio = forms.CharField(max_length=500, required=False, help_text='Optional. Introduce yourself to your colleagues',
                          widget=forms.Textarea(attrs={'rows': 3, }))
    location = forms.CharField(max_length=50, required=False, help_text='Optional.')
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ('profile_pic', 'birth_date', 'bio', 'location',)
