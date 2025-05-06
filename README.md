# GoalsTracker

A minimal Django web app for setting and completing personal goals — like a focused to-do list that keeps you motivated and accountable.

## Features

- User authentication: sign up, log in, log out
- Secure goal creation (C in CRUD)
- Edit/update your goals (U in CRUD)
- Mark goals as completed with a checkbox (R in CRUD)
- Completed goals show strike-through styling
- Only the goal’s owner can view or modify it
- Lightweight interface with clean HTML + minimal JavaScript


### Future Features

- Alternate delete functionality for goal model 
- Filtering user goals
- UX design update
- Reminders 
- dynamic filters (time-based?)
- Daily Quotes for motivation
- Admin User management (Forgot password? Contact admin..?)


## Tech Stack

- Django 5.2
- PostgreSQL (planned)
- HTML5, CSS (no JS frameworks)
- Custom JS for checkbox auto-submit

## Setup

```bash
git clone <repo>
cd goalstracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


## Project Structure 

accounts/       # User signup/login/logout
goals/          # Goal CRUD functionality
templates/      # HTML templates for views
static/         # CSS and JS files


## Bug: Success Message Not Displaying After Goal Deletion

### Context

While implementing the `GoalDeleteView` in Django using `django.views.generic.DeleteView`, I wanted to display a success message to the user after confirming the deletion of a goal.

The `DeleteView` was working correctly — the goal was being deleted and redirected to the goal list — but the message:

```python
messages.success(request, "Goal deleted!")
``` 

never appeared. 

### Diagnosis 

My first approach was to override the delete() method in GoalDeleteView like this:

```python
def delete(self, request, *args, **kwargs):
    messages.success(self.request, "Goal deleted!")
    return super().delete(request, *args, **kwargs)
```

However, Django never called this method. No message appeared, and even inserting a debug `print()` revealed that the method wasn't triggered. Yet, the goal still deleted properly — clearly, Django was falling back to the default behavior.

This strongly suggested that my delete() override was either:

- Incorrectly defined (e.g., missing arguments)

- Not being recognized due to some deeper internal handling


### Solution

Instead of overriding `delete()`, I took a cleaner, more reliable approach by overriding `get_success_url()` — a method Django does call after a successful deletion.

```python
def get_success_url(self):
    messages.success(self.request, "Goal deleted!")
    return reverse_lazy('goals:goal_list')
```

This method runs after the object is deleted and before the user is redirected. Perfect spot to inject feedback like messages.


### Takeaways

- django.views.generic.DeleteView handles deletion via a built-in post() → `delete()` pipeline.

- Overriding `delete()` is possible, but the signature must be exact — and mistakes lead to silent failures.

- `get_success_url()` is a safe, clean alternative for post-action hooks like setting success messages.


### Reflection

This bug took over an hour to identify and resolve. It deepened my understanding of Django’s class-based views and reinforced the principle of relying on the framework’s intended extension points (like `get_success_url()` over `delete()` for non-critical logic).


