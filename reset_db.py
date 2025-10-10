from app import app, db

with app.app_context():
    # Eliminar todas las tablas
    db.drop_all()
    # Crear todas las tablas nuevamente
    db.create_all()
    
    # Crear usuario admin
    from models import Usuario, ConfiguracionAeropuerto
    admin = Usuario(username='admin', rol='admin')
    admin.set_password('123456')
    db.session.add(admin)
    db.session.commit()
    print('Base de datos reiniciada y usuario admin creado')
    
    # Crear configuración del aeropuerto
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
    