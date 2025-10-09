# JoyLine – A Positive Event Timeline

---

## 📖 Project Overview
**JoyLine** is a social web app where users share important life events such as graduations, birthdays, anniversaries, or new jobs.  
Each event becomes a hub of positivity, allowing the community to celebrate and encourage each other.  
Users can look back at their timeline to relive happy moments.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.11+, Django 5.x  
- **Database:** SQLite (default, can switch to PostgreSQL)  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Authentication:** Django built-in auth system  
- **Development Tools:** VS Code, Git, GitHub  

---

## 🏗️ ERD / Data Model

### Entities

**User** (Django built-in)  

**Event**
- `user` (FK → User)  
- `title` (CharField)  
- `description` (TextField)  
- `event_date` (DateField)  
- `created_at` (DateTimeField)  

**Comment**
- `event` (FK → Event)  
- `user` (FK → User)  
- `content` (TextField)  
- `created_at` (DateTimeField)  

**Relationships**
- Each user can create multiple events  
- Each event can have multiple comments  
- Each comment belongs to one user and one event  

### ERD Diagram (Image placeholder)
![ERD Diagram](images/erd.png)  
*Replace with actual ERD image exported from Mermaid Live Editor*

---


## 🧩 User Stories / Features

- **User Authentication:** Users can register, log in, and log out.  
- **Event Management:** Users can create, edit, and delete their own life events.  
- **Timeline:** Users can view all users’ events in a shared timeline sorted by date.  
- **Commenting:** Users can comment on any event.  
- **Admin Controls:** Admins can remove inappropriate comments or manage users.  
- **My Events:** Each user has a “My Events” page showing their events.

---

## 🌟 Stretch Goals (Optional)

- Write and run unit tests (TDD optional)  
- Add image or file uploads for events  
- Implement advanced queries, filters, or pagination  
- Customize user profiles (profile picture, bio, etc.)  
- Email notifications when someone comments on an event  
- Infinite scroll or pagination on the timeline feed

---

## 🔗 External Resources

- [Django Documentation](https://docs.djangoproject.com/)  
- Stack Overflow (for troubleshooting login/logout and form issues)  
- W3Schools HTML/CSS guides  
- MDN Web Docs (for form validation, CSS styling, JS references)

---

## 🛠️ Issues and Project Workflow

- Keep issues active until resolved.  
- Document the solution in the issue thread before closing.  
- Inactive issues for 30+ minutes may be closed automatically.  
- Closed issues cannot be reopened; create a new issue if needed (link to previous).

## ⚙️ Installation Guide
1. Clone the repo:  
```bash
git clone git@github.com:toqasalem18-bot/Capstone-Project.git
cd Capstone-Project\lab-fin\future_mailbox

2.Create a virtual environment :
bash
Copy code
python -m venv venv

3.Activate the virtual environment:
.\venv\Scripts\activate

4.Apply migrations:
python manage.py migrate

5.Create a superuser (for admin access):
python manage.py createsuperuser

6.python manage.py runserver:
python manage.py runserver


