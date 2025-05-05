from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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


class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/goal_form.html'
    success_url = reverse_lazy('goals:goal_list')

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)


@login_required
def toggle_complete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    goal.is_completed = not goal.is_completed
    goal.save()
    return redirect('goals:goal_list')
