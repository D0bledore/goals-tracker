from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Goal
from .forms import GoalForm


# Create your views here.

class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = 'goals/goals_list.html'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    template_name = 'goals/goal_form.html'
    form_class = GoalForm
    success_url = reverse_lazy('goals:goal_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
