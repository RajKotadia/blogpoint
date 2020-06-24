from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def register(request):

	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			print(form.cleaned_data)
			username = form.cleaned_data.get('username')
			form.save()
			messages.success(request, f'Account created for "{username}" !') 
			return redirect('login')

	else:	
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})


# protected route/view
@login_required
def profile(request):
	return render(request, 'users/profile.html', {})