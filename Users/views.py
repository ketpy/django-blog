from django.shortcuts import render , redirect, get_object_or_404
from .models import UserProfile
from .forms import UserUpdateForm, ProfileUpdateForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                messages.info(request, f"Your account has been created and you have been logged in successfully.")
                return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'Users/signup.html', {'form': form})
    

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile = UserProfile.objects.get(user = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile = UserProfile.objects.get(user = request.user)
        profile_url = profile.ProfilePic.url
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form,
        'profile_url' : profile_url,
    }

    return render(request, 'Users/profile.html', context)

@login_required
def logout_user(request):
    logout(request)
    messages.info(request, f'You have successfully logout.')
    return redirect('login')


def PublicProfile(request, username):
    profile = get_object_or_404(User, username = username)
    if request.user.username == profile.username:
        return redirect('/update/profile/')
    return render(request, 'Users/public_profile.html', {'profile' : profile})