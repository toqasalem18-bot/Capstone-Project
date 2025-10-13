# JoyLine – A Positive Event Timeline

## 📖 Project Overview
**JoyLine** is a social web app where users share important life events such as graduations, birthdays, anniversaries, or new jobs.  
Each event becomes a hub of positivity, allowing the community to celebrate and encourage each other.  
Users can look back at their timeline to relive happy moments.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.13+, Django 5.x  
- **Database:** PostgreSQL  
- **Frontend:** HTML, CSS, Bootstrap 5 ,js
- **Authentication:** Django built-in auth system  
- **Development Tools:** VS Code, Git  

---

## 🏗️ ERD / Data Model

### Entities

**User** (Django built-in)  

**Event**
- `user` (FK → User)  
- `created_by` (FK → User, nullable)  
- `title` (CharField)  
- `description` (TextField)  
- `event_date` (DateField)  
- `event_type` (CharField, choices)  
- `custom_event_type` (CharField, nullable)  
- `image` (ImageField, nullable)  
- `hearts` (PositiveIntegerField)  
- `thumbs` (PositiveIntegerField)  
- `tada` (PositiveIntegerField)  
- `created_at` (DateTimeField)  

**Comment**
- `event` (FK → Event)  
- `user` (FK → User)  
- `content` (TextField)  
- `hearts` (PositiveIntegerField)  
- `created_at` (DateTimeField)  

**Notification**
- `recipient` (FK → User)  
- `message` (TextField)  
- `link` (URLField, nullable)  
- `is_read` (BooleanField)  
- `created_at` (DateTimeField)  

### Relationships
- Each user can create multiple events  
- Each event can have multiple comments  
- Each comment belongs to one user and one event  
- Users can react to events with hearts, thumbs, or tada  
- Notifications are created when someone comments or reacts to a user's event  


### ERD Diagram (Image placeholder)
![ERD Diagram](images/pic.png)

*Replace with actual ERD image exported from Mermaid Live Editor*

---


## 🧩 User Stories

1. **As a registered user**, I can create, edit, and delete my own events so that I can maintain my personal timeline.  
2. **As a user**, I can comment on other users’ events to share my thoughts or congratulations.  
3. **As a user**, I can react to events (hearts, thumbs, tada) to express appreciation.  
4. **As a user**, I can view all events in a timeline sorted by date to see other users’ moments.  
5. **As a user**, I can see notifications when someone comments or reacts to my events.  
6. **As an admin**, I can remove inappropriate comments or events to keep the platform safe.  
7. **As a user**, I can browse my own events in a “My Events” page for easy access and management.  

---

## 📱 Responsive Design

- The app uses **CSS Grid** and **Bootstrap 5** to ensure responsiveness across devices.  
- **Desktop:** Events and comments are displayed side by side for a full view.  
- **Tablet:** Layout adjusts to two stacked sections to maintain readability.  
- **Mobile:** Single-column layout for easy scrolling and interaction.  
- Buttons, forms, and images automatically resize to fit different screen widths.  
- Interactive elements (like comment actions) remain accessible and touch-friendly on all devices.

---

## 🌟 Features

- **User Authentication:** Users can register, log in, and log out.  
- **Event Management:** Users can create, edit, and delete their own life events.  
- **Timeline:** Users can view all users’ events in a shared timeline sorted by date.  
- **Commenting:** Users can comment on any event.  
- **Reactions:** Users can react to events with hearts, thumbs, or tada.  
- **Notifications:** Users get notified when someone comments or reacts to their events.  
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
- [Stack Overflow](https://stackoverflow.com/)  
- [W3Schools HTML/CSS Guides](https://www.w3schools.com/)  
- [MDN Web Docs](https://developer.mozilla.org/)  

---

## 🛠️ Issues and Project Workflow
- Keep issues active until resolved.  
- Document the solution in the issue thread before closing.  
- Inactive issues for 30+ minutes may be closed automatically.  
- Closed issues cannot be reopened; create a new issue if needed.

---

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


