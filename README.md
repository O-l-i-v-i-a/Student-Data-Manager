# Student Data Manager

A web-based Student Information Management System built using **Django** and **SQLite**.  
The application allows users to **add, view, update, delete, and filter student records** efficiently.

---

## Features

- Add new student records  
- Edit existing student details  
- Delete student records with confirmation  
- View all students in a tabular format  
- Filter students based on:
  - Annual Income
  - Caste
  - Religion
  - Year of Study
  - Course
- Responsive UI using **Bootstrap 5**
- SQLite database (default Django database)

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, Bootstrap 5
- **Version Control:** Git & GitHub

---

## Project Structure

```text
Student_Data_Manager/
│
├── student_data_manager/    # Project settings
├── students/                # Students app
│   ├── migrations/
│   ├── templates/
│   │   └── students/
│   │       ├── student_list.html
│   │       ├── student_form.html
│   │       └── student_confirm_delete.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md
