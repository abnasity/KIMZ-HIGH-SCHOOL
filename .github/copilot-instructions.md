# =============================================
# School Website - Flask Project Instructions
# =============================================
# 🏫 Purpose:
# A simple Flask web app for a school/institutional website including:
# - Homepage with navbar & footer
# - Mission and Vision statements
# - About the School
# - Management Team
# - Contact Us page with form and flash messages
# - Static CSS for basic styling
#
# ✅ Built with:
# - Flask (Python micro web framework)
# - Jinja2 templates
# - Flash messaging
# - Bootstrap-like custom CSS

# General Guidelines:
- Use Flask 3.1.1
- Use Python 3.13.3
- Always activate `.school` virtual environment before running the application or installing dependencies



🏫 1. Public-Facing School Website (Frontend)

Features:

    Homepage

    Mission & Vision

    About Us

    Contact Page (with form)

    News/Announcements

    Staff Directory

🧑‍💼 2. School Management System (Backend/Admin)

Features:

    Admin & staff login (authentication)

    Role-based access (admin, teacher, student)

    Student management (CRUD)

    Classes & Subjects

    Timetable

    Grades/Results

    Attendance

    Messaging/Notices

    File Uploads (e.g., report cards)

🔧 Tech Stack (Recommended)

    Flask (backend framework)

    Flask-SQLAlchemy (ORM)

    Flask-Login / Flask-Security (auth)

    Jinja2 (templates)

    SQLite or PostgreSQL (database)

    Bootstrap or Tailwind CSS (UI)

    Optionally: AJAX/JS for interactivity

🧱 Suggested Folder Structure

school_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── public.py
│   │   └── admin.py
│   ├── templates/
│   ├── static/
│   └── forms.py
├── migrations/
├── config.py
├── run.py
└── requirements.txt

# 🚀 Running the App:
# 1. Install Flask:
#    pip install Flask
# 2. Run the server:
#    python app.py
# 3. Visit http://localhost:5000 in your browser
#
# 📨 Contact Form:
# - POST /contact
# - Inputs: name, email, message
# - Currently uses Flask flash to simulate a message send
# - Easily extendable with Flask-Mail or email services
#
# 🔧 Future Additions:
# - Flask-Mail integration for contact form
# - Admin dashboard
# - Database support for storing contact entries or staff
# - User login & registration
#
# ✨ Styling Notes:
# - Navbar and footer styled with CSS
# - Uses section anchors (#about, #mission, etc.) for smooth nav
# - Responsive layout can be improved with Bootstrap
#
# 👨‍💻 Copilot Prompts:
# - "Add a new route for /admissions"
# - "Store contact form data in SQLite"
# - "Create a login page using Flask-Login"
# - "Make the navbar responsive using Bootstrap"
# - "Add an admin-only route to post school news"
