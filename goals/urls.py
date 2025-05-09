from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
        path('', views.GoalListView.as_view(), name='goal_list'),
        path('create/', views.GoalCreateView.as_view(), name='goal_create'),
        path('<int:pk>/complete/', views.toggle_complete,
             name='goal_complete'),
        path('<int:pk>/update/', views.GoalUpdateView.as_view(),
             name='goal_update'),
        path('<int:pk>/delete/', views.GoalDeleteView.as_view(),
             name='goal_delete'),
        path('<int:pk>/priority/', views.toggle_priority,
             name='goal_priority'),
        path('<int:pk>/archive/', views.toggle_archive, name='goal_archive'),
    ]
