# Meeting Manager (Django + Bootstrap 5) - Mkutano IO APP

As part if the ALX Capstone project, I built a modern meeting management system built with **Django**, **Python**, and **Bootstrap 5**, allowing users to **schedule, manage, and track meetings** seamlessly.  It features a **Bootstrap 5 interface**, a personalized dashboard, and complete **CRUD functionality**.  
---

## Features

- **User Authentication** — Secure login, signup, and logout using Django’s built-in auth system  
- **Personalized Dashboard** — Displays stats (Upcoming, Ongoing, Ended meetings) for each unique user once signed in  
- **All Meetings Page** — Read-only list of all meetings created by all users   
- **Smart Conflict Detection** — Prevents room double-booking for overlapping times  
- **Dynamic Status Tracking** — Meetings automatically show as *Upcoming*, *Ongoing*, or *Ended*  
- **Search & Filtering** — Search by title, description, or room; filter by status or date range  
- **Pagination** — Smooth navigation through large meeting lists  
- **Timezone Aware** — Automatically localized to `Africa/Nairobi`  
- **Responsive UI** — Built with **Bootstrap 5** for an elegant, mobile-friendly experience  
- **File Uploads** — Attach optional meeting minutes (Not yet implemented fully. Will add to include files such as PPT, PDF and WORD)  

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

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/MukoyaKuya/meeting_manager.git
cd meeting_manager
```

### 2. Create & Activate Virtual Environment

**For Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**If you're using Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3.Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Server
Go to terminal and run:
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Key Functionalities

### Conflict Detection
Before saving a meeting, the app checks if another meeting exists in the same room with overlapping times. If yes, it blocks the save with a warning.

### Meeting Visibility
- *My Meetings* — shows meetings created by the logged-in user.  
- *All Meetings* — read-only list for all users.

### Status Logic
Meetings automatically update their status based on time:
- 🟦 **Upcoming** — Scheduled for later  
- 🟩 **Ongoing** — Currently active  
- 🟥 **Ended** — Finished

### Search & Filters
Users can search meetings by:
- Title / Description  
- Room Name / Organizer  
- Filter by status or date range

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Django 5.x |
| **Frontend** | Bootstrap 5, HTML5, CSS3 |
| **Database** | SQLite |
| **Auth** | Django Auth Framework |
| **Timezone** | Africa/Nairobi |
| **Deployment** |(Not yet deployed)|

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

- Email Notifications for meeting reminders  
- Export meetings as CSV / PDF  
- Calendar View (FullCalendar.js integration)  
- Cloud deployment on Render / Railway  
- Future minutes analysis
- Transcription service in the app
- Proper minutes Archive

---

## Author

**Delton Mukoya Kuya**  
Nairobi County, Kenya  
[GitHub: MukoyaKuya](https://github.com/MukoyaKuya)

---

## License
Licensed under the **MIT License** — free to use, modify, and distribute for educational and non-commercial purposes.

---

## ⭐ Support & Contribution
If you find this project helpful, please **star the repository** ⭐  
Pull requests, issues, and suggestions are welcome!
