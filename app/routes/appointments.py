# routes/appointments.py

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Appointment
from app.forms import AppointmentForm

bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@bp.route('/book', methods=['GET', 'POST'])
@login_required
def book_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment = Appointment(date=form.date.data, user_id=current_user.id, doctor_id=form.doctor.data)
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment booked successfully!')
        return redirect(url_for('index'))
    return render_template('appointments/book_appointment.html', form=form)

@bp.route('/manage')
@login_required
def manage_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('appointments/manage_appointments.html', appointments=appointments)
