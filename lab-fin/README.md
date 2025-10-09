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
