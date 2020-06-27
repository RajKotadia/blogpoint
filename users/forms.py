from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

		widgets = {
			'username': forms.TextInput(attrs={'autocomplete':'off'}),
			'email': forms.EmailInput(attrs={'autocomplete':'off'}),
		}


class UserUpdateForm(forms.ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

		widgets = {
			'username': forms.TextInput(attrs={'autocomplete':'off'}),
			'email': forms.EmailInput(attrs={'autocomplete':'off'}),
		}


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_image', 'bio']
		widgets = {
			'bio': forms.TextInput(attrs={'autocomplete':'off'}),
		}
