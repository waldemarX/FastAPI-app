"""
Configurative file for storage all models.
Alembic creates models from last import to first (adjustable).
"""

from base_class import Base

from auth.models import User, Role
from operations.models import Operation
