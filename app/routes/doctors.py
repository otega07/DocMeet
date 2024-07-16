from flask import Blueprint, render_template
from app.models import Doctor

bp = Blueprint('doctors', __name__, url_prefix='/doctors')

@bp.route('/search')
def search_doctors():
    doctors = Doctor.query.all()
    return render_template('doctors/search_doctors.html', doctors=doctors)

@bp.route('/profile/<int:doctor_id>')
def doctor_profile(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    return render_template('doctors/doctor_profile.html', doctor=doctor)
