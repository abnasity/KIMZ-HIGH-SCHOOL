from app import create_app, db
from app.models import User, Student, Class, Subject, Grade, Attendance, Announcement, ContactMessage

app = create_app()

@app.context_processor
def utility_processor():
    from datetime import datetime
    return dict(now=datetime.utcnow())

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Student': Student,
        'Class': Class,
        'Subject': Subject,
        'Grade': Grade,
        'Attendance': Attendance,
        'Announcement': Announcement,
        'ContactMessage': ContactMessage
    }

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
