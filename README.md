# Meeting Manager — Django Web Application  

A modern meeting management system built with **Django 5** that allows users to **schedule, manage, and view meetings** seamlessly.  
It features **smart time conflict detection**, **meeting status tracking**, and a **a Bootstrap-based interface**.  
Developed as part of the **ALX Back-End Web Development Capstone Project**.

---

## Features

- **User Authentication** — Sign up, login, and logout securely using Django’s auth system  
- **Personalized Dashboard** — Each user sees only their own meetings  
- **All Meetings Page** — Read-only access to meetings created by all users  
- **Conflict Prevention** — Prevents booking the same room at overlapping times  
- **Smart Status Labels** — Meetings show as *Upcoming*, *Ongoing*, or *Ended*  
- **Search & Filtering** — Search by title, description, or room name  
- **Date Range Filters** — Filter meetings by start and end dates  
- **Pagination** — View results in pages for better performance  
- **Timezone Aware** — Automatically localized to `Kenya,Nairobi`  
- **Bootstrap Alerts** — Displays success, warning, and error messages  
- **Responsive UI** — Elegant and mobile-friendly layout using Bootstrap 5

---

## Project Structure

```
meeting_manager/
│
├── meeting_manager/           # Project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── meetings/                  # Core meetings application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── meetings/
│   │   │   ├── meeting_list.html
│   │   │   ├── all_meetings.html
│   │   │   ├── create_meeting.html
│   │   │   ├── meeting_detail.html
│   │   │   ├── meeting_edit.html
│   │   │   └── meeting_confirm_delete.html
│   │   └── registration/
│   │       ├── login.html
│   │       └── signup.html
│   └── admin.py
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── .gitignore
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/MukoyaKuya/meeting_manager.git
cd meeting_manager
```

### 2. Create & Activate a Virtual Environment

**Windows (PowerShell):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin User
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## Key Functionalities

### Conflict Detection
Before a meeting is saved, the system automatically checks:
> “Is there any other meeting in the same room that overlaps with this time?”

If yes, the meeting creation is **blocked** with a friendly error message.

### Meeting Visibility
- Each user sees **only their meetings** on the *My Meetings* page.  
- The *All Meetings* page lists all meetings (read-only view).

### Meeting Status Logic
Meetings dynamically change color & status based on time:
- 🟦 **Upcoming** — Starts in the future  
- 🟩 **Ongoing** — Happening now  
- 🟥 **Ended** — Already finished  

### Search & Filters
Search by:
- Meeting title or description  
- Room name  
- Organizer username  
- Filter by date range or meeting status  

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Django 5.2.7 |
| Frontend | HTML5, Bootstrap 5 |
| Database | SQLite (default) |
| Auth | Django’s built-in User Model |
| Timezone | Africa/Nairobi |
| Deployment-ready | Whitenoise + Gunicorn (optional) |

---

## Requirements

```
Django==5.2.7
tzdata==2025.2
sqlparse==0.5.3
python-decouple==3.8
django-filter==24.3
django-bootstrap4==24.3
```

---

## Roadmap / Future Enhancements

- **Email Notifications** — Send meeting reminders  
- **Export Options** — Download meetings as CSV or PDF  
- **Calendar View** — Visual meeting scheduling (FullCalendar.js)  
- **Role Management** — Admin vs Regular users  
- **Cloud Deployment** — Render / Railway hosting  

---

## Author

**Delton Mukoya**  
Nairobi County, Kenya  
🔗 [GitHub: MukoyaKuya](https://github.com/MukoyaKuya)  


---

## License

This project is licensed under the **MIT License** — free to use, modify, and distribute for educational and non-commercial purposes.

---

### Support & Contribution

If you find this project helpful, please **star the repository** on GitHub.  
Pull requests, issues, and suggestions are welcome!
