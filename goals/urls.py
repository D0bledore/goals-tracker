from django.urls import path
from .views import GoalListView, GoalCreateView, toggle_complete, GoalUpdateView, GoalDeleteView

app_name = 'goals'

urlpatterns = [
        path('', GoalListView.as_view(), name='goal_list'),
        path('create/', GoalCreateView.as_view(), name='goal_create'),
        path('<int:pk>/complete/', toggle_complete, name='goal_complete'),
        path('<int:pk>/update/', GoalUpdateView.as_view(), name='goal_update'),
        path('<int:pk>/delete/', GoalDeleteView.as_view(), name='goal_delete'),
    ]

