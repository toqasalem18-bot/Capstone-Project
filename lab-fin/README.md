# lab-fin
# JoyLine – A Positive Event Timeline

## 📖 Project Overview
JoyLine is a social web application where users share their important life events such as graduations, birthdays, anniversaries, or new jobs. Each event becomes a hub of positivity, allowing the community to celebrate and encourage each other. Users can look back at their timeline to relive happy moments.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.11+, Django 5.x  
- **Database:** SQLite (default, can be changed to PostgreSQL)  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Authentication:** Django built-in auth system  
- **Development Tools:** Visual Studio Code, Git, GitHub  

---

## 🏗️ ERD / Data Model

**Entities:**

**User** (Django built-in)  

**Event**  
- user (FK → User)  
- title (CharField)  
- description (TextField)  
- event_date (DateField)  
- created_at (DateTimeField)  

**Comment**  
- event (FK → Event)  
- user (FK → User)  
- content (TextField)  
- created_at (DateTimeField)  

**Relationships:**  
- Each user can create multiple events.  
- Each event can have multiple comments.  
- Each comment belongs to one user and one event.

**Mermaid ERD Diagram:**
```mermaid
erDiagram
    USER {
        int id PK
        string username
        string email
        datetime date_joined
    }

    EVENT {
        int id PK
        int user_id FK "FK -> USER.id"
        string title
        text description
        date event_date
        datetime created_at
    }

    COMMENT {
        int id PK
        int event_id FK "FK -> EVENT.id"
        int user_id FK "FK -> USER.id"
        text content
        datetime created_at
    }

    USER ||--o{ EVENT : "creates"
    EVENT ||--o{ COMMENT : "has"
    USER ||--o{ COMMENT : "writes"

Clone the repository:

git clone https://github.com/yourusername/joyline.git
cd joyline


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows (PowerShell):

.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Open the browser at http://127.0.0.1:8000/

🧩 User Stories & Feature Documentation

Authentication

Users can register, log in, and log out using Django’s built-in system.

Event Management

Users can create, edit, and delete their own events.

Events appear in a global timeline sorted by date.

Comments

Users can comment on any event.

Comments display the commenter’s username and timestamp.

Timeline / Feed

Home page displays all events sorted by date.

Each event links to a detail page showing all comments.

My Events

Displays all events created by the logged-in user.

Stretch Features (Optional)

Upload images for events.

Add reactions (:heart:, :tada:, :+1:).

Filter events by year or type.

Email notifications for new comments.

Pagination or infinite scroll.

⚠️ Challenges Encountered & Solutions

Authentication Flow:

Challenge: Preventing unauthorized users from editing others’ events.

Solution: Implemented Django’s @login_required and ownership checks in views.

Timeline Sorting & Comments Display:

Challenge: Displaying events in correct date order with latest comments first.

Solution: Used Django QuerySet ordering and related_name to fetch comments efficiently.

Maintaining Template Structure:

Challenge: Updating project features without breaking existing login/logout/signup templates.

Solution: Kept all template names and static files consistent; only updated backend logic and new templates for events/comments.

🔗 External Resources

Django Documentation: https://docs.djangoproject.com/

W3Schools HTML/CSS Guides

MDN Web Docs (CSS, JS, Forms)

Stack Overflow (for troubleshooting specific errors)

🛠️ Issues and Project Workflow

Issues must remain active until resolved.

Close issues immediately once resolved, and document the solution in the thread.

Issues without activity for more than 30 minutes will be closed by instructors.

Closed issues cannot be reopened; create a new issue if needed (include link to prior issue).

📅 Project Plan

Authentication Module – Implement login, logout, signup (reuse current system)

Events CRUD – Add, edit, delete events

Comments CRUD – Add comments to events

Timeline View – Show all events sorted by date

Event Detail – Show event info + all comments + comment form

User “My Events” Page – Display all events of the logged-in user

Optional Stretch Features – Image uploads, filters, reactions, email notifications