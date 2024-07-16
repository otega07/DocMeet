# tests/test_forms.py for the auth and registration forms
from app.routes.auth_forms import RegistrationForm

def test_registration_form():
    form = RegistrationForm(username='newuser', email='newuser@example.com', password='Password123', confirm='Password123')
    assert form.validate()
