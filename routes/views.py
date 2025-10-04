from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import main_bp
from models import Aeronave, Piloto, Vuelo, Confirmacion, Usuario

@main_bp.route('/')
def root():
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    total_a = Aeronave.query.count()
    total_p = Piloto.query.count()
    total_v = Vuelo.query.count()
    total_c = Confirmacion.query.count()
    return render_template('dashboard.html', 
                         total_a=total_a, 
                         total_p=total_p, 
                         total_v=total_v, 
                         total_c=total_c)

@main_bp.route('/admin/aeronaves')
@login_required
def page_aeronaves():
    return render_template('aeronaves.html')

@main_bp.route('/admin/pilotos')
@login_required
def page_pilotos():
    return render_template('pilotos.html')

@main_bp.route('/admin/vuelos', methods=['GET', 'POST'])
@login_required
def page_vuelos():
    pilotos = Piloto.query.all()
    if request.method == 'POST':
        # This is just a view function, actual flight creation is handled by API
        # The copiloto assignment logic should be in the API endpoint
        pass
    return render_template('vuelos.html', pilotos=pilotos)

@main_bp.route('/admin/confirmaciones')
@login_required
def page_confirmaciones():
    return render_template('confirmaciones.html')

@main_bp.route('/admin/usuarios')
@login_required
def page_usuarios():
    if not current_user.rol == 'admin':
        flash('Acceso denegado', 'danger')
        return redirect(url_for('main.dashboard'))
    users = Usuario.query.all()
    return render_template('usuarios.html', users=users)