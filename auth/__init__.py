from flask import Blueprint

# Crear el blueprint
auth_bp = Blueprint('auth', __name__)

# Importar las rutas de autenticación
from . import routes