from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import db, ConfiguracionAeropuerto
from . import config_bp

@config_bp.route('/aeropuerto', methods=['GET', 'POST'])
@login_required
def configuracion_aeropuerto():
    if not current_user.rol == 'admin':
        flash('Acceso denegado. Se requieren permisos de administrador.', 'danger')
        return redirect(url_for('main.dashboard'))

    # Obtener el aeropuerto activo
    config = ConfiguracionAeropuerto.query.filter_by(activo=True).first()
    if not config:
        # Si no hay activo, tomar el primero
        config = ConfiguracionAeropuerto.query.first()
    
    if not config:
        # Crear configuración por defecto si no existe
        config = ConfiguracionAeropuerto(
            nombre='Mi Aeropuerto',
            activo=True
        )
        db.session.add(config)
        db.session.commit()

    if request.method == 'POST':
        try:
            config.nombre = request.form.get('nombre')
            config.codigo_iata = request.form.get('codigo_iata')
            config.codigo_icao = request.form.get('codigo_icao')
            config.director = request.form.get('director')
            config.direccion = request.form.get('direccion')
            config.codigo_postal = request.form.get('codigo_postal')
            config.municipio = request.form.get('municipio')
            config.ciudad = request.form.get('ciudad')
            config.estado = request.form.get('estado')
            config.pais = request.form.get('pais')
            config.telefono = request.form.get('telefono')
            config.email = request.form.get('email')
            config.sitio_web = request.form.get('sitio_web')
            
            db.session.commit()
            flash('Configuración actualizada exitosamente', 'success')
            return redirect(url_for('config.configuracion_aeropuerto'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar la configuración: {str(e)}', 'danger')

    return render_template('config/aeropuerto.html', config=config)