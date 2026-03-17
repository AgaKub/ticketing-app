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






