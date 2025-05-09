from django.shortcuts import render, redirect

# Create your views here.


def homepage_view(request):
    if request.user.is_authenticated:
        return redirect('goals:goal_list')
    return render(request, 'core/homepage.html')
