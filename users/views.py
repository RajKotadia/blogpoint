from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# to register a new user into the system
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			messages.success(request, f'Account created for "{username}" !') 
			return redirect('login')

	else:	
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})


# profile / update profile view
@login_required
def profile(request):
	# handle form submission
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f'Profile successfully updated !') 
			return redirect('profile')

	else:
		# populate the forms with current data
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

		posts = request.user.post_set.all()
		tags = set([ tag.name for p in posts for tag in p.tags.all() ])
		

	context = {
		'user_form': user_form,
		'profile_form': profile_form,
		'posts': posts,
		'tags': tags
	}

	print(user_form.errors)
	print(profile_form.errors)

	return render(request, 'users/profile.html', context)