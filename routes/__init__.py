from flask import Blueprint

# Crear los blueprints
main_bp = Blueprint('main', __name__)
config_bp = Blueprint('config', __name__, url_prefix='/config')

# Importar las vistas después de crear los blueprints
from . import views
from . import config