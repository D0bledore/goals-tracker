from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Goal
from .forms import GoalForm


# Create your views here.

class GoalListView(LoginRequiredMixin, TemplateView):
    template_name = 'goals/goal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        priority_filter = self.request.GET.get('priority')

        all_goals = Goal.objects.filter(user=self.request.user).order_by('-created_at')

        if priority_filter in ['high', 'medium', 'low']:
            all_goals = all_goals.filter(priority=priority_filter)

        context['active_goals'] = all_goals.filter(is_archived=False)
        context['archived_goals'] = all_goals.filter(is_archived=True)
        return context


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    template_name = 'goals/goal_form.html'
    form_class = GoalForm
    success_url = reverse_lazy('goals:goal_list')


    def form_valid(self, form):
        print("CREATE METHOD CALLED")
        form.instance.user = self.request.user
        messages.success(self.request, "Created a new goal!")
        return super().form_valid(form)


class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/goal_form.html'
    success_url = reverse_lazy('goals:goal_list')

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Goal updated!")
        return super().form_valid(form)


class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    template_name = 'goals/goal_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, "Goal deleted!")
        return reverse_lazy('goals:goal_list')

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)


@login_required
def toggle_complete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    goal.is_completed = not goal.is_completed
    goal.save()
    return redirect('goals:goal_list')


@login_required
def toggle_priority(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    next_priority = {'low': 'medium', 'medium': 'high', 'high': 'low'}
    goal.priority = next_priority.get(goal.priority, 'low')
    goal.save()
    return redirect('goals:goal_list')


@login_required
def toggle_archive(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    goal.is_archived = not goal.is_archived
    goal.save()
    return redirect('goals:goal_list')
