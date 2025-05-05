from django.urls import path
from .views import GoalListView, GoalCreateView

app_name = 'goals'

urlpatterns = [
        path('', GoalListView.as_view(), name='goal_list'),
        path('create/', GoalCreateView.as_view(), name='goal_create'),
    ]

