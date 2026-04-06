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

### Step 2.5 – Define the Event Model

At this step the first data model of the system will be introduced.

The Event model will represent a single event created by a promoter.

This model will later store essential event information such as:

- event name
- venue
- date
- ticket price
- ticket quantity
- description

At this stage the model is only defined conceptually.  
The actual implementation will follow in the next step.

This is the first step toward building the core business logic of the ticketing system.

### Step 2.6 – Implement the Event Model

At this step the Event model will be implemented in the `events` app.

The model will define the structure of event data stored in the database.

The Event model will include fields such as:

- name (event name)
- venue (event location)
- date (event date)
- price (ticket price)
- capacity (number of tickets available)
- description (event details)

This step introduces the first custom database model in the system.

#### Update – Event Model Design Adjustment

During the design review it was identified that a single price per event is not sufficient for real-world ticketing scenarios.

Most events include multiple ticket types (e.g. Early Bird, Regular, VIP), each with different pricing and availability.

To support this, the data model will be adjusted:

- the Event model will no longer contain price and capacity
- a new model (TicketType) will be introduced
- each Event will be able to have multiple TicketTypes

This adjustment improves the flexibility and realism of the system and aligns it with real promoter needs.

### Step 2.8 – Prepare Database Migrations for Event and TicketType

At this step the custom models defined in the `events` app will be translated into database changes.

Django uses migrations to convert model definitions into database table structures.

Running migrations for these models will create:

- an Event table
- a TicketType table
- a relationship between TicketType and Event through a foreign key

This step turns the first custom business models of the system into real database structures.

### Step 2.9 – Create Initial Migrations for Events App

The first custom migrations for the `events` app were created successfully.

Django generated an initial migration file containing instructions to create:

- the Event model
- the TicketType model

This confirms that the model definitions are valid and ready to be applied to the database.

### Step 2.10 – Apply Migrations for Events App

At this step the previously created migrations will be applied to the database.

Applying migrations will create the actual database tables for:

- Event
- TicketType

It will also establish the relationship between these models through a foreign key.

This step completes the process of translating model definitions into a working database structure.

### Step 2.11 – Events App Database Tables Created

The migrations for the `events` app were successfully applied.

This created the first custom business tables in the database:

- Event
- TicketType

The relationship between TicketType and Event was also established through a foreign key.

This marks the completion of the first custom data model implementation in the project.



## Stage 3 – Admin Interface

This stage introduces the Django admin panel as a way to interact with the system data.

The admin panel allows creating, editing, and managing data directly through a web interface.

### Step 3.1 – Register Models in Admin

At this step the Event and TicketType models will be registered in the Django admin panel.

Registering models allows them to be visible and manageable through the admin interface.

This enables:

- creating events
- adding ticket types
- managing data without writing code

### Step 3.4 – Improve Event Admin with Inline Ticket Types

At this step the admin interface for Event will be improved.

The goal is to display related TicketType records directly inside the Event admin page.

This will make the admin workflow more natural by allowing ticket types to be managed from within the corresponding event.

This improves usability and reflects the real business relationship between events and ticket types.


## Stage 4 – Public Interface

This stage introduces the user-facing part of the application.

The goal is to allow users (buyers) to:

- view available events
- open event details
- see available ticket types

This is the first step toward building the ticket purchasing experience.

### Step 4.1 – Create Event List View

A view was created to display all available events.

This view retrieves all Event objects from the database and passes them to a template.

The page is accessible at:

/ (root URL)

### Step 4.2 – Create Event List Template

A template was created to display the list of events.

The template shows:

- event name
- venue
- date

Each event is clickable and links to its detail page.

### Step 4.3 – Create Event Detail View

A view was created to display a single event.

The view retrieves:

- event details
- related ticket types

Ticket types are accessed using the related_name defined in the model.

### Step 4.4 – Fix Reverse Relationship

An error occurred when accessing ticket types from the Event model.

The issue was caused by missing related_name in the ForeignKey.

The model was updated:

ForeignKey(Event, related_name='ticket_types')

This allows access via:

event.ticket_types.all()

### Step 4.5 – Create Event Detail Template

A template was created to display:

- event name
- venue
- date
- ticket types

Each ticket type displays:

- name
- price
- available quantity

### Step 4.6 – Add Buy Button

A "Buy" button was added next to each ticket type.

This is the first step toward implementing ticket purchasing.

No functionality is implemented yet.

The button prepares the UI for future interaction (form submission).


## Stage 4 – Buyer Interface

This stage introduces the first buyer-facing purchase interaction.

### Step 4.1 – Prepare Buy Button Flow

At this step the Buy button will stop being only a visual element and will begin passing the selected ticket type and quantity to the next step of the purchase flow.

The goal is to connect ticket selection with the beginning of checkout.

### Step 4.2 – Buy Button Interaction

The Buy button was connected to the ticket selection logic.

When clicked, it reads:
- selected quantity
- ticket type

and confirms the selection via a temporary alert.

This step validates that user interaction is correctly captured before moving to checkout implementation.

### Step 4.3 – Multi-Ticket Selection Flow

The buyer-facing event page was redesigned to support selecting multiple ticket types in a single order.

The previous approach used a separate Buy button for each ticket type, which did not support mixed selections well.

This was replaced with:

- quantity selectors starting from 0
- no per-ticket Buy button
- one shared “Continue to checkout” button

This allows the buyer to build a ticket selection across multiple ticket types before moving forward.

### Step 4.4 – Shared Checkout Entry

The shared “Continue to checkout” button was connected to the selected ticket quantities.

Only ticket types with quantity greater than 0 are passed to checkout.

If no tickets are selected, checkout is not allowed.

This establishes the first basket-style selection flow on the buyer side.


### Step 4.5 – Multi-Ticket Checkout View

The checkout step was updated to support multiple selected ticket types.

Instead of expecting a single `ticket` and `qty`, the checkout logic now reads multiple ticket selections from the request and displays them as a grouped summary.

This allows the buyer to review the full ticket selection before continuing.

### Step 4.6 – Multi-Ticket Email Step

The email step was updated to support multiple selected ticket types.

The selected tickets and their quantities are preserved when moving from checkout to the email step.

This keeps the purchase flow consistent for mixed ticket selections.

### Step 4.7 – Email Justification Restored

The email step includes a clear explanation of why the buyer’s email is required.

The wording explains that the ticket and payment confirmation will be sent to the provided email address.

A checkbox was also included to confirm agreement to receive ticket- and event-related information.

This improves trust, clarity, and legal readiness in the purchase flow.


### Step 4.8 – Payment Step as Order Review

The payment step will be upgraded from a placeholder into an order review page.

At this step, the goal is to display the buyer’s current order before real payment integration is added.

The payment step should show:

- selected ticket types
- selected quantities
- buyer email

This creates a clear pre-payment stage in the purchase flow and prepares the application for future payment integration.

I agree to receive my ticket and event-related information and accept the 
<a href="/privacy-policy/" target="_blank">Privacy Policy</a>


### Step 4.9 – Minimal Privacy Policy (MVP)

A minimal privacy policy page was introduced to support transparent handling of personal data.

At this stage, the application collects only the buyer’s email address, which is used exclusively for:

- sending the ticket
- providing payment confirmation
- sharing essential event-related information

The privacy policy clearly communicates that:

- the email is not used for marketing purposes
- data is not shared with third parties except where necessary to process the purchase

A link to the privacy policy was added to the email step, and user consent is required before continuing.

This establishes a basic legal and trust layer for the purchase flow.

### Step 4.10 – Backend Total Calculation

The payment step was upgraded to calculate the total order value in the backend.

Instead of relying on frontend data, ticket prices are now retrieved from the database.

For each selected ticket type:
- the system reads the ticket price
- multiplies it by the selected quantity
- calculates a subtotal

All subtotals are then summed to produce the final order total.

The payment page now displays:
- ticket name
- quantity
- unit price
- subtotal per ticket type
- total order value

This ensures that pricing is accurate and cannot be manipulated from the frontend.


## Stage 5 – Order Layer

This stage introduces the first order-related business structure in the system.

The goal is to create a real Order model that will store the buyer’s purchase before payment integration is added.

This will allow the application to move from temporary flow logic to persistent order handling.

### Step 5.1 – Prepare Order Model

At this step the order layer is defined conceptually.

The Order model will represent a buyer’s purchase and will later connect:

- buyer email
- selected tickets
- order total
- payment status

This model will become the foundation for future payment integration and ticket generation.

### Step 5.2 – Link Order to Event

The Order model was extended with a relationship to Event.

This reflects the rule that one order belongs to one event, even when the event contains multiple ticket types (for example, a multi-day festival with different ticket options).

The relationship was added as a foreign key from Order to Event.

During migration, the field was temporarily made nullable to avoid conflicts with existing rows in the database.

This prepares the order layer for real order creation in the purchase flow.

### Step 5.3 – Introduce Order Items

The Order model currently stores only summary-level information such as email, total, and event.

To properly represent what the customer purchased, a new structure is needed.

Each order can contain multiple ticket types with different quantities.

To support this, an OrderItem model will be introduced.

OrderItem will represent a single line in the order and will connect:
- the order
- the ticket type
- the quantity

This allows the system to store detailed purchase data and prepares the foundation for ticket generation and entry validation.

### Step 5.4 – Create OrderItem Model

A new OrderItem model was introduced to store the detailed contents of an order.

While the Order model stores summary-level information such as event, email, and total, the OrderItem model stores the individual ticket selections made by the buyer.

Each OrderItem connects:
- the order
- the ticket type
- the selected quantity

This allows the application to preserve exactly what was purchased and prepares the system for ticket generation, payment reconciliation, and entry validation.

### Step 5.5 – Save Order Items in the Purchase Flow

The payment step was refactored to store detailed ticket selections as OrderItem records.

Instead of only creating an Order summary, the system now also creates one OrderItem for each selected ticket type.

Each OrderItem stores:
- the order
- the ticket type
- the selected quantity

The payment step was improved to:

- validate selected tickets before creating the order
- determine the correct event from the selected tickets
- ensure all selected tickets belong to the same event
- convert quantities to integers before saving

This establishes a proper order structure and allows the application to preserve exactly what the buyer purchased.

### Step 5.6 – Prepare Cart Reservation Logic

The next step in the user purchase flow is to introduce temporary reservation logic.

At this stage, tickets are reduced immediately when an order is created, even if payment is not completed.

This is acceptable for early testing, but not sufficient for a real ticketing flow.

The system will therefore move toward a reservation-based approach where:

- an order is initially created as pending
- selected tickets are reserved only for a limited time
- the buyer must complete payment within that reservation window
- if payment is not completed in time, the reservation expires and tickets are released back to availability

For the MVP direction, the planned reservation window is 10 minutes.

A maximum ticket limit per order will also be introduced to reduce the risk of one unfinished order blocking too much inventory.


### Step 5.8 – Add Backend Validation for Ticket Selection Limits

The payment step was updated to enforce ticket selection limits in the backend.

In addition to the buyer-facing selector limits, the backend now validates that:

- the selected quantity does not exceed available ticket stock
- the selected quantity does not exceed the maximum allowed quantity per ticket type in one order (10)

If either rule is broken, the purchase flow is stopped and redirected.

This ensures that ticket selection rules are enforced even if frontend restrictions are bypassed.

### Step 5.9 – Trigger Reservation Cleanup from Buyer Flow

The expired-order cleanup logic was connected to buyer-facing views so that reservation status is refreshed during normal use of the application.

The cleanup function is now triggered when the buyer opens the event page.

This allows the system to:

- detect expired pending orders
- release reserved tickets back to stock
- mark those orders as expired

Testing confirmed that the cleanup logic works correctly when triggered from the buyer flow and that the updated status becomes visible in the admin dashboard after refresh.

### Step 5.10 – Replace Silent Redirects with Clear Buyer Feedback

The purchase flow currently uses redirects when ticket selection is invalid, for example when the requested quantity exceeds stock availability or exceeds the maximum allowed quantity.

While this protects the system technically, it does not explain the problem to the buyer.

The next improvement is to replace silent redirects with clear feedback messages that tell the buyer what went wrong and what action to take.

This will improve trust, reduce confusion, and make the purchase flow easier to complete.

### Step 5.11 – Add Clear Buyer Error Messages

The purchase flow was updated to give the buyer clear feedback when ticket selection is invalid.

Instead of silently redirecting to the homepage, the backend now returns the buyer to the event page with an error indicator in the URL.

The event page displays a clear message when:

- the maximum ticket limit per ticket type is exceeded
- the requested number of tickets is greater than available stock

This improves trust and makes the buyer flow easier to understand and complete.

### Step 5.12 – Redirect Buyer to the Correct Event After Validation Errors

The purchase flow was improved so that backend validation errors no longer redirect to a hardcoded event page.

Instead, the system now uses the event connected to the selected ticket type and redirects the buyer back to the correct event automatically.

This makes the flow consistent and prepares the application for multiple events running in the same system.


### Step 6.1 – Refactor Ticket Stock into Total and Available Quantity

The TicketType model was refactored so that stock is now represented with two separate fields:

- total_quantity
- available_quantity

This replaces the previous single quantity field, which mixed original stock and remaining stock in a confusing way.

The new structure allows the system to represent:

- original ticket capacity per ticket type
- remaining availability
- sold quantity, calculated as total_quantity minus available_quantity

The buyer flow and backend stock checks were updated to use available_quantity.

The admin view was also improved to show total stock, available stock, and sold quantity clearly for promoters.

### Step 6.2 – Separate Reservation from Completed Sale

The next stage of the ticketing logic is to separate temporary reservation from completed sale.

At the current stage, available ticket quantity is reduced immediately when a pending order is created.

This is useful for early testing, but it mixes two different business states:

- reservation
- completed purchase

The system will now move toward clearer logic:

- pending orders will represent temporary reservation
- paid orders will represent completed sale
- expired orders will release reserved tickets
- available ticket quantity should reflect active reservations and completed sales in a controlled way

This change will make the ticketing flow closer to real production logic and prepare the system for future payment integration.

### Step 6.4 – Stop Reducing Stock on Pending Orders

The ticketing logic was updated so that creating a pending order no longer reduces available ticket quantity.

Pending orders now represent reservations rather than completed sales.

This separates reservation from completed purchase and prepares the system for proper payment handling.

The next step will be to account for reserved tickets in pending orders when calculating availability, to prevent overselling.

### Step 6.5 – Add Reservation-Aware Availability Validation

The backend validation logic was improved so that pending reservations are now taken into account when checking ticket availability.

When the buyer attempts to continue to checkout, the system now calculates effective availability as:

- available ticket quantity
- minus tickets currently held by active pending orders

This prevents overselling when stock has not yet been permanently reduced for unpaid reservations.

The next step will be to reflect the same reservation-aware availability in the buyer-facing event page.

### Step 6.6 – Show Reservation-Aware Availability in Buyer Flow

The buyer-facing event page was updated to display real availability based on active reservations.

For each ticket type, the system now calculates effective availability as:

- available ticket quantity
- minus tickets currently held by active pending orders

This effective availability is now used in the event page to:

- display the number of tickets still available
- limit the quantity selector

This aligns the buyer-facing view with the backend validation logic and prevents misleading stock information during active reservation periods.



