from flask import Blueprint, request, jsonify
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
            'tipo_aeronave': a.tipo_aeronave
        } for a in items])
    # Accept both JSON and FormData
    if request.is_json:
        data = request.json or {}
    else:
        data = request.form.to_dict()
    
    a = Aeronave(
        matricula=data.get('matricula'), 
        modelo=data.get('modelo'), 
        fabricante=data.get('fabricante'), 
        capacidad=int(data.get('capacidad', 0)) if data.get('capacidad') else None, 
        tipo_aeronave=data.get('tipo_aeronave')
    )
    db.session.add(a)
    db.session.commit()
    return jsonify({'msg':'ok','id':a.aeronave_id}),201

@api_bp.route('/aeronaves/<int:id>', methods=['GET','PUT','DELETE'])
def aeronave_item(id):
    a = Aeronave.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'aeronave_id': a.aeronave_id,'matricula': a.matricula,'modelo': a.modelo,'fabricante': a.fabricante,'capacidad': a.capacidad,'tipo_aeronave': a.tipo_aeronave})
    if request.method == 'PUT':
        # Accept both JSON and FormData
        if request.is_json:
            data = request.json or {}
        else:
            data = request.form.to_dict()
        
        a.matricula = data.get('matricula', a.matricula)
        a.modelo = data.get('modelo', a.modelo)
        a.fabricante = data.get('fabricante', a.fabricante)
        if data.get('capacidad'):
            a.capacidad = int(data.get('capacidad'))
        a.tipo_aeronave = data.get('tipo_aeronave', a.tipo_aeronave)
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
        return jsonify([{'piloto_id': p.piloto_id,'nombre': p.nombre,'licencia': p.licencia,'tipo_licencia': p.tipo_licencia,'horas_vuelo': p.horas_vuelo,'nacionalidad': p.nacionalidad} for p in items])
    data = request.json or {}
    p = Piloto(nombre=data.get('nombre'), licencia=data.get('licencia'), tipo_licencia=data.get('tipo_licencia'), horas_vuelo=data.get('horas_vuelo',0), nacionalidad=data.get('nacionalidad'))
    db.session.add(p); db.session.commit()
    return jsonify({'msg':'ok','id':p.piloto_id}),201

@api_bp.route('/pilotos/<int:id>', methods=['GET','PUT','DELETE'])
def piloto_item(id):
    p = Piloto.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'piloto_id': p.piloto_id,'nombre': p.nombre,'licencia': p.licencia,'tipo_licencia': p.tipo_licencia,'horas_vuelo': p.horas_vuelo,'nacionalidad': p.nacionalidad})
    if request.method == 'PUT':
        data = request.json or {}
        p.nombre = data.get('nombre', p.nombre)
        p.licencia = data.get('licencia', p.licencia)
        p.tipo_licencia = data.get('tipo_licencia', p.tipo_licencia)
        p.horas_vuelo = data.get('horas_vuelo', p.horas_vuelo)
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
                # allow date or datetime prefix
                query = query.filter(Vuelo.fecha_salida.like(f"{fecha}%"))
            except Exception:
                pass
        if aeronave_id:
            query = query.filter_by(id_aeronave=aeronave_id)
        if piloto_id:
            query = query.filter_by(id_piloto=piloto_id)
        items = query.all()
        def todict(v):
            return {'id_vuelo': v.id_vuelo,'codigo_vuelo': v.codigo_vuelo,'origen': v.origen,'destino': v.destino,'fecha_salida': v.fecha_salida.isoformat(),'fecha_llegada': v.fecha_llegada.isoformat() if v.fecha_llegada else None,'id_aeronave': v.id_aeronave,'id_piloto': v.id_piloto,'estado': v.estado}
        return jsonify([todict(x) for x in items])
    data = request.json or {}
    fs = data.get('fecha_salida')
    fl = data.get('fecha_llegada')
    fs_dt = datetime.fromisoformat(fs) if fs else datetime.utcnow()
    fl_dt = datetime.fromisoformat(fl) if fl else None
    v = Vuelo(
        codigo_vuelo=data.get('codigo_vuelo'), 
        origen=data.get('origen'), 
        destino=data.get('destino'), 
        fecha_salida=fs_dt, 
        fecha_llegada=fl_dt, 
        id_aeronave=data.get('id_aeronave'), 
        id_piloto=data.get('id_piloto'), 
        estado=data.get('estado','Programado')
    )
    db.session.add(v); db.session.commit()
    return jsonify({'msg':'ok','id':v.id_vuelo}),201

@api_bp.route('/vuelos/<int:id>', methods=['GET','PUT','DELETE'])
def vuelo_item(id):
    v = Vuelo.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'id_vuelo': v.id_vuelo,'codigo_vuelo': v.codigo_vuelo,'origen': v.origen,'destino': v.destino,'fecha_salida': v.fecha_salida.isoformat(),'fecha_llegada': v.fecha_llegada.isoformat() if v.fecha_llegada else None,'id_aeronave': v.id_aeronave,'id_piloto': v.id_piloto,'estado': v.estado})
    if request.method == 'PUT':
        data = request.json or {}
        v.codigo_vuelo = data.get('codigo_vuelo', v.codigo_vuelo)
        v.origen = data.get('origen', v.origen)
        v.destino = data.get('destino', v.destino)
        v.estado = data.get('estado', v.estado)
        if data.get('fecha_salida'):
            v.fecha_salida = datetime.fromisoformat(data.get('fecha_salida'))
        if data.get('fecha_llegada'):
            v.fecha_llegada = datetime.fromisoformat(data.get('fecha_llegada'))
        if data.get('id_aeronave'):
            v.id_aeronave = data.get('id_aeronave')
        if data.get('id_piloto'):
            v.id_piloto = data.get('id_piloto')
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
