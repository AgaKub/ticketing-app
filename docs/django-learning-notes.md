# Django Learning Notes – Ticketing App Project

This document collects the key concepts learned while building the ticketing backend.

---

# 1. Django Project vs Django App

Django separates the system into two levels:

## Django Project

The **project** is the main container for the backend.

It contains:

- global settings
- database configuration
- URL routing
- server configuration
- installed applications

In this project the Django project folder is:


config


Example structure:


ticketing-app
│
├── config
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── manage.py


The project handles **system configuration**, not business logic.

---

## Django Apps

Apps contain the **actual features of the system**.

Examples for the ticketing platform:


events
tickets
checkin
payments


Apps contain code like:


models.py
views.py
urls.py
admin.py


Each app represents **one functional module** of the system.

Example future structure:


ticketing-app
│
├── config
│
├── events
├── tickets
├── checkin
│
├── docs
├── manage.py


---

# 2. The Django Database

Django stores application data in a database.

In development Django uses **SQLite**, which stores everything in one file:


db.sqlite3


This file contains all database tables.

Example future data:


events
tickets
buyers
check-ins


Example event record:

| id | event | venue | date |
|----|------|------|------|
| 1 | Indie Night | Underground Club | 2026-07-12 |

---

# 3. Why the Database Already Exists

Even before creating our own models, Django already needs a database for its internal systems.

Django provides built-in applications such as:


django.contrib.admin
django.contrib.auth
django.contrib.sessions
django.contrib.contenttypes


These require database tables like:


auth_user
auth_group
django_admin_log
django_session
django_migrations


Those tables are stored in:


db.sqlite3


---

# 4. Django Architecture: Models, Views, URLs

Django works with three main layers.

---

## Models (Data Layer)

Models define the **structure of stored data**.

Example future model:

```python
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)

This creates a table in the database.

Relationship:

models.py → database tables → db.sqlite3

Models define what data exists.

Views (Logic Layer)

Views contain the application logic.

They decide what happens when a user makes a request.

Example:

def event_list(request):
    events = Event.objects.all()
    return HttpResponse("List of events")

Views decide:

what data to load

what response to return

Views represent system behavior.

URLs (Routing Layer)

URLs connect web addresses to views.

Example:

urlpatterns = [
    path("events/", views.event_list),
]

This means:

/events → run event_list view

URLs act as the navigation system of the application.

5. How a Request Flows Through Django

When a user interacts with the system, Django processes the request like this:

User browser
     ↓
URL routing
     ↓
View (logic)
     ↓
Model (database access)
     ↓
Response returned to user

Example in the ticketing system:

User opens /events
      ↓
urls.py routes request
      ↓
view loads events
      ↓
model reads from database
      ↓
view returns response
6. Mental Model

A helpful analogy:

Models → the archive (data storage)

Views → the employees handling requests

URLs → the receptionist directing visitors

Each part has a single responsibility, which keeps the system organized and scalable.

7. Current Project State

Project structure currently:

ticketing-app
│
├── config
├── docs
├── venv
├── db.sqlite3
├── manage.py
└── README.md

Development stages are documented in:

docs/development-log.md

This file records every step of building the backend.


