from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Register Page
def register(request):
    # Check POST
    if request.method == 'POST':
        # Django register form
        form = UserRegisterForm(request.POST)
        # Check if is valid
        if form.is_valid():
            # Hash password
            form.save()
            # Take username and Sanitize then
            username = form.cleaned_data.get('username')
            # Send message
            messages.success(
                request, 'Votre compte a été créé! Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        # If not valid show only form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Only logged user can use that
@login_required
# Profile Page
def profile(request):
    # Check POST
    if request.method == 'POST':
        # Fill our form with the right data from user
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES,  instance=request.user.profile)
        # Validation data from Form and save then
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Send message
            messages.success(
                request, 'Votre compte a été mis à jour.')
            return redirect('profile')
    else:
        # Instance is for update our form
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    # That I send into page
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)
