from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from app.models import User, Student, Class, Subject, Grade, Attendance, Announcement
from app.forms import AnnouncementForm, GradeForm, AttendanceForm
from app import db
from datetime import datetime
from functools import wraps

bp = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role not in ['admin', 'teacher']:
            flash('You do not have permission to access this page.', 'error')
            return redirect(url_for('public.index'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    student_count = Student.query.count()
    class_count = Class.query.count()
    announcement_count = Announcement.query.count()
    recent_activities = []  # You can add recent activities logic here
    return render_template('admin/dashboard.html', title='Dashboard',
                         student_count=student_count,
                         class_count=class_count,
                         announcement_count=announcement_count,
                         recent_activities=recent_activities)

@bp.route('/students')
@login_required
@admin_required
def students():
    page = request.args.get('page', 1, type=int)
    students = Student.query.paginate(page=page, per_page=10, error_out=False)
    return render_template('admin/students.html', title='Students', students=students)

@bp.route('/grades', methods=['GET', 'POST'])
@login_required
@admin_required
def grades():
    form = GradeForm()
    if form.validate_on_submit():
        grade = Grade(
            student_id=form.student.data,
            subject_id=form.subject.data,
            score=form.score.data,
            term=form.term.data
        )
        db.session.add(grade)
        db.session.commit()
        flash('Grade has been recorded successfully.', 'success')
        return redirect(url_for('admin.grades'))
    
    grades = Grade.query.order_by(Grade.date.desc()).all()
    return render_template('admin/grades.html', title='Grades', form=form, grades=grades)

@bp.route('/attendance', methods=['GET', 'POST'])
@login_required
@admin_required
def attendance():
    form = AttendanceForm()
    if form.validate_on_submit():
        attendance = Attendance(
            student_id=form.student.data,
            date=form.date.data,
            status=form.status.data
        )
        db.session.add(attendance)
        db.session.commit()
        flash('Attendance has been marked.', 'success')
        return redirect(url_for('admin.attendance'))
    
    today = datetime.utcnow().date()
    attendance_records = Attendance.query.filter_by(date=today).all()
    return render_template('admin/attendance.html', title='Attendance', 
                         form=form, attendance_records=attendance_records)

@bp.route('/announcements', methods=['GET', 'POST'])
@login_required
@admin_required
def announcements():
    form = AnnouncementForm()
    if form.validate_on_submit():
        announcement = Announcement(
            title=form.title.data,
            content=form.content.data,
            author_id=current_user.id
        )
        db.session.add(announcement)
        db.session.commit()
        flash('Announcement has been posted.', 'success')
        return redirect(url_for('admin.announcements'))
    
    announcements = Announcement.query.order_by(Announcement.timestamp.desc()).all()
    return render_template('admin/announcements.html', title='Manage Announcements', 
                         form=form, announcements=announcements)
