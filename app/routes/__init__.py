# routes/__init__.py
from .users import bp as users_bp
from .appointments import bp as appointments_bp
from .doctors import bp as doctors_bp

__all__ = ['users_bp', 'appointments_bp', 'doctors_bp']
