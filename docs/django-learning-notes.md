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


# Django Learning Notes

## 1. The basic Django flow – how the “house” works

I want to think about Django like a house with rooms and doors.

### Main idea

A buyer opens a page in the browser.

The request then moves through Django in this order:

1. URL
2. View
3. Template
4. Browser output

If data is involved, the view also talks to:

5. Model
6. Database

So the real flow is:

Browser → URL → View → Model/Database → View → Template → Browser

---

## 2. What each part does

### URL
The URL decides **which view should handle the request**.

Example:
- `/`
- `/event/1/`
- `/checkout/`

There are usually 2 levels:
- project URLs (`config/urls.py`)
- app URLs (`events/urls.py`)

I should remember:
- `config/urls.py` = main router
- `events/urls.py` = routes inside the events app

---

### View
The view is the **logic room**.

It decides:
- what data to load
- what checks to make
- which template to show
- what values to pass to the template

Example:
- get all events
- get one event
- read ticket selections
- redirect if something is missing

---

### Model
The model defines the **data structure**.

Example:
- Event
- TicketType

The model is the structure of what is stored in the database.

---

### Database
The database stores the actual data.

Example:
- Indie Night
- Early Bird
- VIP
- quantities
- prices

The model defines the shape.
The database stores the real records.

---

### Template
The template is the **HTML page with Django placeholders**.

Example:
- `event_list.html`
- `event_detail.html`
- `checkout.html`

The template shows what the user sees.

The template should mostly display data, not contain heavy logic.

---

## 3. Proper development flow in Django

When I build a new feature, I should usually think in this order:

### A. First: decide what the user should do
Example:
- see events
- select tickets
- continue to checkout

This is product / UX thinking.

---

### B. Then: decide what data is needed
Example:
- event
- ticket types
- quantity
- email

If new data is needed, I may need to update the model.

---

### C. Then: update or create the model
Example:
- add field
- create new model
- change relationship

If I change a model, I must remember:

1. `python manage.py makemigrations`
2. `python manage.py migrate`

---

### D. Then: create or update the view
The view should:
- receive the request
- get data
- validate data
- send data to the template

---

### E. Then: register the URL
If the page or action is new, I must connect it in:
- `events/urls.py`
- sometimes also `config/urls.py`

Without URL, the browser cannot reach the view.

---

### F. Then: create or update the template
The template shows the output.

Example:
- event page
- checkout page
- email step

---

### G. Then: test the full flow in browser
I should click through the whole path:
- start page
- event page
- checkout
- email
- payment

This helps catch missing corners in the “house”.

---

### H. Then: document
Update:
- `development-log.md`
- `django-learning-notes.md`

---

### I. Then: Git
Save progress:

1. `git add .`
2. `git commit -m "message"`
3. `git push`

---

## 4. My checklist when something does not work

When Django breaks, I should check in this order:

### 1. Is the virtual environment active?
Do I see:

      `(venv)`

in PowerShell?

      ---

### 2. Is the server running?
Did I run:

      `python manage.py runserver`

      ---

### 3. Is the URL registered?
Check:
      - `config/urls.py`
      - `events/urls.py`

      ---

### 4. Does the view exist and have the correct name?
Maybe the URL points to the wrong view or the view name is different.

      ---

### 5. Does the template file exist in the correct folder?
Correct pattern:

      `events/templates/events/file_name.html`

      ---

### 6. Is the template using the correct variables?
Example:
      - `tickets` vs `ticket_data`
      - `tickettype_set` vs `ticket_types`

      ---

### 7. If model changed: did I run migrations?
Need both:
      - `makemigrations`
      - `migrate`

      ---

## 5. PowerShell basics for this project

### Go to project folder
      ```powershell
      cd C:\Coding\ticketing-app


Activate virtual environment
      .\venv\Scripts\activate
What I should see
      (venv) PS C:\Coding\ticketing-app>

      Run server
      python manage.py runserver

      Stop server
      Ctrl + C

      Create migrations
      python manage.py makemigrations

      Apply migrations
      python manage.py migrate

      Create admin user
      python manage.py createsuperuser


6. Basic Git commands for this project

      Check what changed
      git status

      Add all changes
      git add .

      Add only one folder
      git add docs

      Commit changes
      git commit -m "message"

      Push to GitHub
      git push

      See commit history
      git log --oneline

7. Important mental models I want to remember
     
      Model = data structure
      Migration = instruction to change database
      View = logic
      Template = what user sees
      URL = door to the correct room
      Admin = internal management tool
      Public page = buyer view

8. House logic – how rooms connect

I want to think like this:

      URL = corridor
      View = decision room
      Model = storage rules
      Database = warehouse
      Template = shop window
      Admin = back office

So the request flows through the house, not randomly.

I must always ask:

      which room is missing?
      which door is not connected?
      which room got data but did not pass it forward?

9. Practical feature-building order I should follow

      When adding a new feature, ask:

            What should the user do?
            What data is needed?
            Do I need a model change?
            Do I need migrations?
            Do I need a new view?
            Do I need a new URL?
            Do I need a new template?
            Did I test the full flow?
            Did I document it?
            Did I commit it?

10. One sentence summary

      Django works as a connected system:

      Browser → URL → View → Model/Database → View → Template → Browser

      If something breaks, one of these connections is missing.