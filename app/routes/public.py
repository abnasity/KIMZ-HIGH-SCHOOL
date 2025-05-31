from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.forms import ContactForm
from app.models import ContactMessage, Announcement, User
from app import db

bp = Blueprint('public', __name__)

@bp.route('/')
def index():
    announcements = Announcement.query.order_by(Announcement.timestamp.desc()).limit(3).all()
    return render_template('public/index.html', title='Home', announcements=announcements)

@bp.route('/about')
def about():
    return render_template('public/about.html', title='About Us')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('public.contact'))
    return render_template('public/contact.html', title='Contact Us', form=form)

@bp.route('/announcements')
def announcements():
    page = request.args.get('page', 1, type=int)
    announcements = Announcement.query.order_by(Announcement.timestamp.desc())\
        .paginate(page=page, per_page=10, error_out=False)
    return render_template('public/announcements.html', title='Announcements', 
                         announcements=announcements)

@bp.route('/staff')
def staff():
    teachers = User.query.filter_by(role='teacher').all()
    return render_template('public/staff.html', title='Our Staff', teachers=teachers)
