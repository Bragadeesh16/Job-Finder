from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import (
    UserRegisterForm, UserProfileForm, LoginForm,
    OrganizationRegisterForm, OrganizationProfileForm
)
from account.models import UserProfile, Organization,CustomUser


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, form.errors or 'Invalid credentials')
    return render(request, 'login.html', {'form': form})

def user_register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            cuser = CustomUser.objects.get(email=email)
            userprofile = UserProfile.objects.create(user = cuser)
            userprofile.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "You are signed in successfully.")
            return redirect("home")
        else:
            messages.error(request, form.errors)

    return render(request, 'User-Register.html', {'form': form})


def organization_register(request):
    form = OrganizationRegisterForm()
    if request.method == "POST":
        form = OrganizationRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_organization = True
            user.save()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            organization_name = form.cleaned_data['organization_name']
            user = CustomUser.objects.get(email=email)
            organization = Organization.objects.create(user = user,name = organization_name)
            organization.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "You are signed in successfully.")
            return redirect("home")

    return render(request, 'Organization-Register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    if hasattr(request.user, 'organization'):
        user_organization = request.user.organization
        context = {'user_organization': user_organization}
    else:

        user_profile = UserProfile.objects.get(user=request.user)
        context = {'user_profile': user_profile}

    return render(request, 'Profile.html', context)


@login_required
def edit_profile_view(request): 
    user = CustomUser.objects.get(email = request.user.email)

    if user.is_organization:
        organization  = Organization.objects.get(user = user)
        form = OrganizationProfileForm(instance=organization)
        if request.method == 'POST':
            form = OrganizationProfileForm(request.POST, instance=organization)
            if form.is_valid():
                form.save()
                messages.success(request, 'Organization profile updated successfully!')
                return redirect('home')

        context = {'form': form}
    
    else:
        profile = UserProfile.objects.get(user = user)
        form = UserProfileForm(instance=profile)

        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('home')

        context = {'form': form}

    return render(request, 'Edit-Profile.html', context)