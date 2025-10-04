from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from models import db, Aeronave, Piloto, Vuelo, Confirmacion, Usuario, ConfiguracionAeropuerto
from datetime import datetime

api_bp = Blueprint('api', __name__)

# Aeronaves
@api_bp.route('/aeronaves', methods=['GET','POST'])
def aeronaves():
    if request.method == 'GET':
        items = Aeronave.query.all()
        return jsonify([{
            'aeronave_id': a.aeronave_id,
            'matricula': a.matricula,
            'modelo': a.modelo,
            'fabricante': a.fabricante,
            'capacidad': a.capacidad,
            'tipo_aeronave': a.tipo_aeronave,
            'imagen': a.imagen
        } for a in items])
    # Accept both JSON and FormData
    try:
        upload_folder = os.path.join('static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)

        if request.is_json:
            data = request.json or {}
            files = None
        else:
            data = request.form.to_dict()
            files = request.files

        matricula = (data.get('matricula') or '').strip()
        modelo = (data.get('modelo') or '').strip()
        if not matricula or not modelo:
            return jsonify({'msg': 'matricula y modelo son requeridos'}), 400

        capacidad_val = None
        raw_cap = data.get('capacidad')
        if raw_cap not in (None, '', '0'):
            try:
                capacidad_val = int(raw_cap)
            except (TypeError, ValueError):
                return jsonify({'msg': 'capacidad inválida'}), 400

        imagen_filename = None
        if files and 'imagen' in files and files['imagen']:
            file = files['imagen']
            if file.filename:
                filename = secure_filename(file.filename)
                imagen_filename = filename
                file.save(os.path.join(upload_folder, filename))

        a = Aeronave(
            matricula=matricula,
            modelo=modelo,
            fabricante=(data.get('fabricante') or None),
            capacidad=capacidad_val,
            tipo_aeronave=(data.get('tipo_aeronave') or None),
            imagen=imagen_filename
        )
        db.session.add(a)
        db.session.commit()
        return jsonify({'msg':'ok','id':a.aeronave_id}),201
    except Exception as e:
        db.session.rollback()
        try:
            # Provide safer string for error
            err = str(e)
        except Exception:
            err = 'error'
        return jsonify({'msg': f'error al guardar: {err}'}), 500

@api_bp.route('/aeronaves/<int:id>', methods=['GET','PUT','DELETE'])
def aeronave_item(id):
    a = Aeronave.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'aeronave_id': a.aeronave_id,'matricula': a.matricula,'modelo': a.modelo,'fabricante': a.fabricante,'capacidad': a.capacidad,'tipo_aeronave': a.tipo_aeronave,'imagen': a.imagen})
    if request.method == 'PUT':
        # Accept both JSON and FormData
        upload_folder = os.path.join('static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        if request.is_json:
            data = request.json or {}
            files = None
        else:
            data = request.form.to_dict()
            files = request.files
        
        a.matricula = data.get('matricula', a.matricula)
        a.modelo = data.get('modelo', a.modelo)
        a.fabricante = data.get('fabricante', a.fabricante)
        if data.get('capacidad'):
            a.capacidad = int(data.get('capacidad'))
        a.tipo_aeronave = data.get('tipo_aeronave', a.tipo_aeronave)
        if files and 'imagen' in files and files['imagen'] and files['imagen'].filename:
            file = files['imagen']
            filename = secure_filename(file.filename)
            file.save(os.path.join(upload_folder, filename))
            a.imagen = filename
        db.session.commit()
        return jsonify({'msg':'updated'})
    db.session.delete(a)
    db.session.commit()
    return jsonify({'msg':'deleted'})

# Pilotos
@api_bp.route('/pilotos', methods=['GET','POST'])
def pilotos():
    if request.method == 'GET':
        items = Piloto.query.all()
        return jsonify([{
            'piloto_id': p.piloto_id,
            'nombre': p.nombre,
            'licencia': p.licencia,
            # Campos no existentes en el modelo, devueltos para compatibilidad del frontend
            'tipo_licencia': None,
            'horas_vuelo': p.horas_vuelo,
            'nacionalidad': None
        } for p in items])
    data = request.json or {}
    p = Piloto(
        nombre=data.get('nombre'),
        licencia=data.get('licencia'),
        horas_vuelo=data.get('horas_vuelo', 0)
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({'msg':'ok','id':p.piloto_id}),201

@api_bp.route('/pilotos/<int:id>', methods=['GET','PUT','DELETE'])
def piloto_item(id):
    p = Piloto.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({
            'piloto_id': p.piloto_id,
            'nombre': p.nombre,
            'licencia': p.licencia,
            'tipo_licencia': p.tipo_licencia,
            'horas_vuelo': p.horas_vuelo,
            'nacionalidad': p.nacionalidad
        })
    if request.method == 'PUT':
        data = request.json or {}
        p.nombre = data.get('nombre', p.nombre)
        p.licencia = data.get('licencia', p.licencia)
        p.horas_vuelo = data.get('horas_vuelo', p.horas_vuelo)
        p.tipo_licencia = data.get('tipo_licencia', p.tipo_licencia)
        p.nacionalidad = data.get('nacionalidad', p.nacionalidad)
        db.session.commit()
        return jsonify({'msg':'updated'})
    db.session.delete(p); db.session.commit()
    return jsonify({'msg':'deleted'})

# Vuelos with filters
@api_bp.route('/vuelos', methods=['GET','POST'])
def vuelos():
    if request.method == 'GET':
        fecha = request.args.get('fecha')
        aeronave_id = request.args.get('aeronave_id')
        piloto_id = request.args.get('piloto_id')
        query = Vuelo.query
        if fecha:
            try:
                query = query.filter(Vuelo.fecha_salida.like(f"{fecha}%"))
            except Exception:
                pass
        if aeronave_id:
            query = query.filter_by(aeronave_id=aeronave_id)
        if piloto_id:
            query = query.filter_by(piloto_id=piloto_id)
        items = query.all()
        def todict(v):
            return {
                'id_vuelo': v.vuelo_id,
                'codigo_vuelo': v.numero_vuelo,
                'origen': v.origen,
                'destino': v.destino,
                'fecha_salida': v.fecha_salida.isoformat() if v.fecha_salida else None,
                'fecha_llegada': v.fecha_llegada.isoformat() if v.fecha_llegada else None,
                'id_aeronave': v.aeronave_id,
                'id_piloto': v.piloto_id,
                'id_copiloto': v.copiloto_id,
                'observaciones': v.observaciones
            }
        return jsonify([todict(x) for x in items])
    data = request.json or {}
    fs = data.get('fecha_salida')
    fl = data.get('fecha_llegada')
    try:
        fs_dt = datetime.fromisoformat(fs) if fs else datetime.utcnow()
    except Exception:
        return jsonify({'msg': 'fecha_salida inválida (ISO 8601 esperado)'}), 400
    try:
        fl_dt = datetime.fromisoformat(fl) if fl else None
    except Exception:
        return jsonify({'msg': 'fecha_llegada inválida (ISO 8601 esperado)'}), 400
    v = Vuelo(
        numero_vuelo=data.get('numero_vuelo') or data.get('codigo_vuelo'),
        origen=data.get('origen'),
        destino=data.get('destino'),
        fecha_salida=fs_dt,
        fecha_llegada=fl_dt,
        aeronave_id=data.get('aeronave_id'),
        piloto_id=data.get('piloto_id'),
        copiloto_id=data.get('copiloto_id'),
        observaciones=data.get('observaciones')
    )
    try:
        db.session.add(v); db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': f'Error al guardar vuelo: {str(e)}'}), 400
    return jsonify({'msg':'ok','id':v.vuelo_id}),201

@api_bp.route('/vuelos/<int:id>', methods=['GET','PUT','DELETE'])
def vuelo_item(id):
    v = Vuelo.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({
            'id_vuelo': v.vuelo_id,
            'codigo_vuelo': v.numero_vuelo,
            'origen': v.origen,
            'destino': v.destino,
            'fecha_salida': v.fecha_salida.isoformat() if v.fecha_salida else None,
            'fecha_llegada': v.fecha_llegada.isoformat() if v.fecha_llegada else None,
            'id_aeronave': v.aeronave_id,
            'id_piloto': v.piloto_id,
            'id_copiloto': v.copiloto_id,
            'observaciones': v.observaciones
        })
    if request.method == 'PUT':
        data = request.json or {}
        if 'numero_vuelo' in data or 'codigo_vuelo' in data:
            v.numero_vuelo = data.get('numero_vuelo', data.get('codigo_vuelo', v.numero_vuelo))
        v.origen = data.get('origen', v.origen)
        v.destino = data.get('destino', v.destino)
        if data.get('fecha_salida'):
            v.fecha_salida = datetime.fromisoformat(data.get('fecha_salida'))
        if data.get('fecha_llegada'):
            v.fecha_llegada = datetime.fromisoformat(data.get('fecha_llegada'))
        if data.get('id_aeronave') is not None:
            v.aeronave_id = data.get('id_aeronave')
        if data.get('id_piloto') is not None:
            v.piloto_id = data.get('id_piloto')
        if 'id_copiloto' in data:
            v.copiloto_id = data.get('id_copiloto')
        if 'observaciones' in data:
            v.observaciones = data.get('observaciones')
        db.session.commit()
        return jsonify({'msg':'updated'})
    db.session.delete(v); db.session.commit()
    return jsonify({'msg':'deleted'})

# Confirmaciones
@api_bp.route('/confirmaciones', methods=['GET','POST'])
@login_required
def confirmaciones():
    if request.method == 'GET':
        items = Confirmacion.query.all()
        return jsonify([{'confirmacion_id': c.confirmacion_id,'vuelo_id': c.vuelo_id,'estado': c.estado,'notas': c.notas} for c in items])
    data = request.json or {}
    
    # Verificar permisos: solo operadores autorizados (no piloto ni invitado)
    if current_user.rol in ['piloto', 'invitado']:
        return jsonify({'msg':'Acceso denegado. Solo operadores autorizados pueden confirmar vuelos.'}), 403
    
    c = Confirmacion(vuelo_id=data.get('vuelo_id'), estado=data.get('estado','Pendiente'), notas=data.get('notas'))
    db.session.add(c); db.session.commit()
    return jsonify({'msg':'ok','id':c.confirmacion_id}),201


# Usuarios (minimal)
@api_bp.route('/usuarios', methods=['GET','POST'])
def usuarios():
    if request.method == 'GET':
        items = Usuario.query.all()
        return jsonify([{'id': u.id, 'username': u.username, 'rol': u.rol} for u in items])
    data = request.json or {}
    username = data.get('username'); password = data.get('password'); rol = data.get('rol','admin')
    if not username or not password:
        return jsonify({'msg':'username and password required'}),400
    u = Usuario(username=username, rol=rol)
    u.set_password(password)
    db.session.add(u); db.session.commit()
    return jsonify({'msg':'ok','id':u.id}),201

# Usuario actual
@api_bp.route('/usuario-actual', methods=['GET'])
@login_required
def usuario_actual():
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'rol': current_user.rol
    })

# Configuración del Aeropuerto
@api_bp.route('/configuracion-aeropuerto', methods=['GET'])
def configuracion_aeropuerto():
    config = ConfiguracionAeropuerto.query.first()
    if not config:
        # Crear configuración por defecto si no existe
        config = ConfiguracionAeropuerto(
            nombre='Mi Aeropuerto',
            ciudad='Ciudad',
            municipio='Municipio',
            estado='Estado',
            pais='México'
        )
        db.session.add(config)
        db.session.commit()
    
    return jsonify({
        'nombre': config.nombre,
        'ciudad': config.ciudad,
        'municipio': config.municipio,
        'estado': config.estado,
        'pais': config.pais,
        'codigo_iata': config.codigo_iata,
        'codigo_icao': config.codigo_icao,
        'director': config.director,
        'direccion': config.direccion,
        'codigo_postal': config.codigo_postal,
        'telefono': config.telefono,
        'email': config.email,
        'sitio_web': config.sitio_web
    })
