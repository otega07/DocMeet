from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from app.models import Appointment, Doctor
from app.routes.appointments_forms import AppointmentForm

bp = Blueprint('appointments', __name__)

@bp.route('/appointments', methods=['GET', 'POST'])
@login_required
def book_appointment():
    form = AppointmentForm()
    doctors = Doctor.query.all()
    form.doctor_id.choices = [(doctor.id, doctor.name) for doctor in doctors]
    if form.validate_on_submit():
        appointment = Appointment(
            date=form.date.data,
            user_id=current_user.id,
            doctor_id=form.doctor_id.data
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Your appointment has been booked!')
        return redirect(url_for('appointments.book_appointment'))
    return render_template('book_appointment.html', form=form)

@bp.route('/manage_appointments', methods=['GET'])
@login_required
def manage_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('manage_appointments.html', appointments=appointments)
