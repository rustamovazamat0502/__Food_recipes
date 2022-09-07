from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import RegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import Group, User
from recipe.decorators import admin_only


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            group = Group.objects.get(name="users")
            user.groups.add(group)
            messages.success(request, f"Account Created For {username} Successfully !")
            return redirect("login")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "users/register.html", context)


def show_users(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "users/users.html", context)


def update_user(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, "User Updated Successfully !")
            return redirect("users")
    else:
        form = RegistrationForm(instance=user)
    context = {"form": form}
    return render(request, 'users/register.html', context)


def delete_user(request, pk):
    user = User.objects.get(id=pk)
    if request.method == "POST":
        user.delete()
        messages.warning(request, "User deleted successfully !")
        return redirect("users")
    context = {}
    return render(request, "users/delete_user.html", context)


def profile(request):
    return render(request, "users/profile.html")


def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated !")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        'p_form': p_form,
        "title": "User Profile"
    }

    return render(request, "users/update_profile.html", context)
