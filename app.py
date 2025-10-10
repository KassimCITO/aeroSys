from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from models import db, Usuario, ConfiguracionAeropuerto

# Inicialización de Flask
app = Flask(__name__)
app.secret_key = '7f8e2d5301ff8133b1b26117299c5c7c1c11544990ddf0e4ea1398d8cfe53ff9'
app.config.from_object(Config)

# Inicializar extensiones
db.init_app(app)
migrate = Migrate(app, db)

# Configurar Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, int(user_id))

# Importar y registrar blueprints después de crear app
from routes import main_bp, config_bp
from auth.routes import auth_bp
from api import api_bp
from reports import reports_bp

app.register_blueprint(main_bp)
app.register_blueprint(config_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(reports_bp, url_prefix='/reports')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            # Asegurar que existe el admin
            admin = Usuario.query.filter_by(username='admin').first()
            if not admin:
                admin = Usuario(username='admin', rol='admin')
                admin.set_password('123456')
                db.session.add(admin)
                db.session.commit()
                print('Usuario admin creado: admin/123456')
        except Exception as e:
            print(f'Error al inicializar la base de datos: {e}')
        # Creación de datos iniciales del aeropuerto...
        try:
            config = ConfiguracionAeropuerto.query.first()
            if not config:
                config = ConfiguracionAeropuerto(
                    nombre='Aeropuerto de la ciudad de Apatzingán',
                    codigo_iata='CIT',
                    codigo_icao='MCIT',
                    director='Cte. Miguel Estrada García',
                    direccion='Av. Morelos Pte. 3333, Km.1.5',
                    codigo_postal='60600',
                    municipio='Apatzingán',
                    ciudad='Apatzingán de la Constitución',
                    estado='Michoacán',
                    pais='México',
                    telefono='+52 (453) 101.5588',
                    email='juan_colorado@outlook.com',
                    sitio_web='https://github.com/KassimCITO/aeroSys'
                )
                db.session.add(config)
                db.session.commit()
                print('Configuración del aeropuerto creada')
        except Exception as e:
            print(f'Error al inicializar la configuración del aeropuerto: {e}')

    app.run(host='0.0.0.0', port=5000, debug=True)
