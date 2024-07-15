from flask_wtf import FlaskForm
from wtforms import DateTimeField, SelectField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    date = DateTimeField('Date', validators=[DataRequired()])
    doctor_id = SelectField('Doctor', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Book Appointment')
