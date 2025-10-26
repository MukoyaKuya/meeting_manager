# Meeting Manager (Django + Bootstrap 5) — Mkutano IO App

As part of the **ALX Capstone Project**, I built a modern meeting management system using **Django, Python, and Bootstrap 5**.  
The app allows users to schedule, manage, and track meetings seamlessly through a clean, responsive interface and includes a personalized dashboard with full CRUD functionality.

---

## Features

- **User Authentication** — Secure login, signup, and logout using Django’s built-in authentication system  
- **Personalized Dashboard** — Displays meeting stats (Upcoming, Ongoing, Ended) for each signed-in user  
- **All Meetings Page** — Read-only list of all meetings created by all users  
- **Smart Conflict Detection** — Prevents room double-booking for overlapping times  
- **Dynamic Status Tracking** — Meetings automatically show as Upcoming, Ongoing, or Ended  
- **Search & Filtering** — Search by title, description, or room; filter by status or date range  
- **Pagination** — Smooth navigation through large meeting lists  
- **Timezone Aware** — Automatically localized to Africa/Nairobi  
- **Responsive UI** — Built with Bootstrap 5 for a mobile-friendly, elegant experience  
- **File Uploads** — Attach optional meeting minutes (planned feature for PPT, PDF, and DOC files)

---

## Project Structure

```
meeting_manager/
│
├── meeting_manager/           # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── meetings/                  # Core application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── meetings/
│   │   │   ├── home.html
│   │   │   ├── my_meetings.html
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

### 2. Create and Activate Virtual Environment
**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Because the database is shipped empty, you must create the tables before running the app:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (for Admin Access)
```bash
python manage.py createsuperuser
```
Provide a username, email (optional), and password when prompted.
This allows admin to add rooms, remove users and update upcoming meetings

### 6. Run the Server
```bash
python manage.py runserver
```
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Accessing the Admin Dashboard

Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
Log in using the superuser credentials you created.

If you see an error such as:

```
OperationalError: no such table: django_session
```

Run migrations again:

```bash
python manage.py migrate
```

To promote an existing user to admin:
```python
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.get(username='your_username')
user.is_staff = True
user.is_superuser = True
user.save()
exit()
```

---

## Key Functionalities

### Conflict Detection
Before saving a meeting, the app checks if another meeting exists in the same room with overlapping times. If yes, it blocks the save with a warning.

### Meeting Visibility
- **My Meetings** — shows meetings created by the logged-in user  
- **All Meetings** — read-only list visible to all users

### Status Logic
Meetings automatically update their status based on the current time:
- 🟦 Upcoming — scheduled for later  
- 🟩 Ongoing — currently active  
- 🟥 Ended — finished

### Search & Filters
Users can search and filter meetings by:
- Title or Description  
- Room name or Organizer  
- Status or Date range

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Django 5.x |
| Frontend | Bootstrap 5, HTML5, CSS3 |
| Database | SQLite |
| Authentication | Django Auth Framework |
| Timezone | Africa/Nairobi |
| Deployment | Not yet deployed |

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

- Email notifications for meeting reminders  
- Export meetings as CSV or PDF  
- Calendar view (FullCalendar.js integration)  
- Cloud deployment on Render or Railway  
- Automatic minutes analysis  
- Transcription services integration  
- Dedicated minutes archive system  
- **API Integration:** development of a RESTful API (using Django REST Framework) to connect with an Android/Kotlin mobile app for real-time meeting management and synchronization between web and mobile platforms  

---

## Planned API Architecture

The upcoming API will expose secure, RESTful endpoints to allow external and mobile clients to interact with the Meeting Manager system.

### Overview
- Framework: Django REST Framework (DRF)  
- Authentication: Token-based or JWT authentication  
- Data exchange: JSON over HTTPS  

### Example Endpoints
| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/v1/meetings/` | GET | Retrieve all meetings |
| `/api/v1/meetings/<id>/` | GET | Retrieve specific meeting details |
| `/api/v1/meetings/create/` | POST | Create a new meeting |
| `/api/v1/users/login/` | POST | Authenticate and issue token |
| `/api/v1/users/signup/` | POST | Register new user |

### Android/Kotlin Integration Plan
- The Android app will consume these endpoints via Retrofit or Ktor client.  
- User sessions will be managed using secure token storage (EncryptedSharedPreferences).  
- The mobile app will provide offline caching and sync with the Django backend when online.  

This design ensures smooth communication between web and mobile interfaces under a unified API layer.

---

## Author

**Delton Mukoya Kuya**  
Nairobi County, Kenya  
GitHub: [MukoyaKuya](https://github.com/MukoyaKuya)

---

## License

Licensed under the **MIT License** — free to use, modify, and distribute for educational and non-commercial purposes.

---

## ⭐ Support & Contribution
If you find this project helpful, please **star the repository** ⭐  
Pull requests, issues, and suggestions are welcome!
