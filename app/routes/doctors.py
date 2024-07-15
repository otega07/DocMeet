from flask import Blueprint, render_template
from app.models import Doctor

bp = Blueprint('doctors', __name__)

@bp.route('/doctors', methods=['GET'])
def list_doctors():
    doctors = Doctor.query.all()
    return render_template('search_doctors.html', doctors=doctors)
