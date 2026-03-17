# Ticketing App – Development Log

Stage 0 – Preparation
Stage 1 – Backend foundation
Stage 2 – Event model
Stage 3 – Ticket model
Stage 4 – Sales flow
Stage 5 – Ticket validation
Stage 6 – Payment integration



## Stage 0 – Project Preparation

At this stage the goal is to prepare the foundation of the project before writing any backend code.

This includes:

- creating the GitHub repository
- preparing the local project folder
- setting up basic project documentation
- defining the purpose and structure of the system

The project aims to build a lightweight ticketing system for small event promoters who want to sell tickets without relying on large ticketing platforms.

The backend will eventually support:

- event creation
- ticket sales
- ticket tracking
- ticket validation at the entrance

The backend will be implemented using Django.

No application logic is implemented yet. This stage focuses purely on preparing the project environment and documentation.

## Step 0.1 – Development Documentation

Created the project documentation structure.

Added a `docs` directory and a `development-log.md` file to record the evolution of the system and document each development stage.

Purpose:
To keep track of architectural decisions and development steps while building the project.

## Step 0.2 – Backend Framework Selection

At this step the backend framework for the project is defined.

The ticketing system backend will be built using Django.

Django is chosen because it provides:

- a mature and stable web framework
- a built-in database ORM
- a powerful administrative interface
- strong security features
- rapid development capabilities

This framework will serve as the foundation for managing events, tickets, and ticket validation in the system.

## Step 0.3 – Backend Project Structure

At this step the high-level backend structure of the project is defined.

The backend will consist of a Django project that will contain multiple apps responsible for different parts of the system.

The first app planned for the system will manage events and tickets.

The backend will eventually support:

- event creation and management
- ticket generation
- ticket sales tracking
- ticket validation at event entry

At this stage no Django project has been created yet.  
This step documents the intended backend structure before implementation begins.

## Step 0.4 – Preparing Django Project Initialization

At this step the project is ready to begin backend implementation.

The Django framework has been selected and the backend structure has been conceptually defined.

The next action will be the initialization of the Django project that will serve as the foundation of the ticketing backend.

This will create the core backend environment where future apps, models, and business logic will be implemented.



## Stage 1 – Backend Initialization

This stage marks the beginning of the backend implementation of the ticketing system.

The goal of this stage is to initialize the Django backend project that will serve as the core of the application.

During this stage the following will happen:

- creation of the Django project
- verification that the Django server runs locally
- preparation of the backend environment for future apps

No business logic will be implemented yet.  
This stage focuses only on establishing the working backend foundation.

### Step 1.1 – Django Project Creation

This step begins the technical implementation of the backend.

The Django project will be created in the repository to serve as the core backend application.

The Django project will provide:

- the main application configuration
- the backend server
- the base structure for future Django apps
- database connection and configuration

This project will later host apps responsible for managing events, tickets, and ticket validation.

### Step 1.2 – Verify Django Server

The Django project already exists in the repository under the `config` directory.

At this step the goal is to verify that the Django development server runs correctly in the local environment.

Running the server confirms that:

- the Django installation is working
- the project configuration is correct
- the backend environment is ready for further development


### Step 1.3 – Run Django Development Server

The Django development server was started to verify that the backend runs correctly.

The server started successfully, confirming that:

- the Django project is correctly configured
- the local development environment is working

A message indicated that there are unapplied migrations, which means the database structure has not yet been initialized.

This will be handled in the next step.

### Step 1.4 – Apply Database Migrations

At this step the initial database structure will be created.

Django includes built-in applications (such as admin, authentication, and sessions) that require database tables.

Migrations are used to apply these structures to the database.

Running migrations will:

- create the necessary database tables
- initialize the database schema
- prepare the system for storing data

This step will complete the basic backend setup required for further development.

### Step 1.5 – Database Initialization Completed

Database migrations were successfully applied.

All default Django tables for built-in applications (admin, authentication, sessions, content types) were created in the SQLite database.

This confirms that:

- the database is correctly configured
- the backend is fully initialized
- the system is ready to store application data

The backend foundation is now complete.


## Stage 2 – First Backend App

This stage begins the creation of the first application-specific backend module.

The goal of this stage is to create the first Django app that will hold the core business logic of the ticketing system.

This app will become the place where event-related functionality will be developed.

During this stage the following will happen:

- creation of the first Django app
- registration of the app in the Django project
- preparation for future models such as events and tickets

At this point no custom business models are implemented yet.  
This stage begins the modular structure of the backend.

### Step 2.1 – Define the Events App

The first backend app of the system will be the `events` app.

This app will be responsible for the event-related part of the ticketing system.

Its purpose is to provide a dedicated module for the future implementation of:

- event creation
- event details
- event management
- relationships between events and tickets

At this step the app is only being defined conceptually.  
The technical creation of the app will happen next.

### Step 2.2 – Create the Events App

In this step the first Django app will be created.

The app name will be `events`.

This app will become a separate module within the project and will contain all logic related to events.

Creating the app will generate a new folder with the standard Django structure, including:

- models.py
- views.py
- admin.py
- apps.py
- migrations/

This establishes the modular architecture of the backend.

### Step 2.3 – Register the Events App

After creating the `events` app, the Django project must be informed that this app is part of the system.

This is done by adding the app to the `INSTALLED_APPS` list in the project settings.

Registering the app allows Django to:

- recognize the app as part of the project
- include its models in migrations
- make its admin configuration available
- prepare it for future development

At this step no business logic is added yet.  
The goal is only to connect the new app to the Django project.

### Step 2.4 – Verify App Registration

After adding the `events` app to INSTALLED_APPS, the app is now fully registered in the Django project.

This means Django recognizes the app as part of the system and will include it in:

- database migrations
- admin panel configuration
- future development processes

At this stage no models are defined yet, so no new migrations are expected.

This step confirms that the modular structure of the backend is working correctly.





