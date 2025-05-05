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


## Project Structure 

accounts/       # User signup/login/logout
goals/          # Goal CRUD functionality
templates/      # HTML templates for views
static/         # CSS and JS files
