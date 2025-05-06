from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('goals:goal_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
