# Meeting Manager (Django)

**Meeting Manager** is a web-based application that enables users to schedule, manage, and track meetings seamlessly. It’s part of a broader system designed to enhance team collaboration and optimize room utilization within organizations.

---

## Overview

**Meeting Manager** simplifies collaboration by allowing authenticated users to schedule and manage their own meetings while granting administrators full control over room management and moderation. It’s ideal for organizations, schools, or co-working spaces.

---

## Core Features

* **User Roles & Access Control**

  * **Admins:** Create, edit, and delete meeting rooms and any meeting.
  * **Users:** Schedule, view, and manage their own meetings.
* **Room Management:** Define meeting rooms with name, location, and capacity.
* **Meeting Scheduling:** Title, description, date/time, room assignment, and organizer tracking.
* **Authentication:** Secure login and role-based authorization.
* **Admin Dashboard:** View, filter, and manage rooms and meetings.
* **Responsive UI:** Clean, mobile-ready templates using Django’s template system.

---

## Tech Stack

* **Backend:** Django 5.2, Python 3.11+
* **Database:** SQLite ( will switch later to PostgreSQL/MySQL).
* **Frontend:** Django Templates + Bootstrap 
* **Version Control:** Git & GitHub

---

## Project Structure

```text
meeting_manager/
├─ manage.py
├─ meeting_manager/
│  ├─ settings.py
│  ├─ urls.py
│  └─ ...
├─ meetings/
│  ├─ models.py
│  ├─ views.py
│  ├─ admin.py
│  ├─ urls.py
│  ├─ templates/meetings/
│  └─ migrations/
└─ templates/registration/
```

---

##  Data Model

```text
User ─┬─< Meeting.organizer (FK)
      │
      └── MeetingRoom
```

* **MeetingRoom:** name, location, capacity
* **Meeting:** title, room, start/end time, organizer, description

---

## Permissions

| Action              | User | Admin |
| ------------------- | ---- | ----- |
| View rooms          | ✅    | ✅     |
| Create room         | ❌    | ✅     |
| Manage any meeting  | ❌    | ✅     |
| Manage own meetings | ✅    | ✅     |

---

## Deployment Ready

Designed for easy deployment and scaling. The configuration supports environment variables and production-ready database switching.

---

## Future Enhancements

* Room availability validation & booking conflict checks
* Calendar integration (iCal, Google Calendar)
* Notifications (email/SMS)
* REST API for mobile & web clients

---

## Author

**Delton Mukoya**
[LinkedIn](https://www.linkedin.com/in/mukoya-kuya) · [GitHub](https://github.com/MukoyaKuya)

---

> Part of My **ALX Back‑End Web Development** journey.
