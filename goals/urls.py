from django.urls import path
from .views import GoalListView, GoalCreateView, toggle_complete

app_name = 'goals'

urlpatterns = [
        path('', GoalListView.as_view(), name='goal_list'),
        path('create/', GoalCreateView.as_view(), name='goal_create'),
        path('<int:pk>/complete/', toggle_complete, name='goal_complete'),
    ]

