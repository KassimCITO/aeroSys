from app import app
from models import db, Aeronave, Piloto, Vuelo, Confirmacion, Usuario, ConfiguracionAeropuerto
from datetime import datetime, timedelta
import random

def seed_data():
    with app.app_context():
        print("🗑️  Eliminando tablas existentes...")
        db.drop_all()
        print("🏗️  Creando nuevas tablas...")
        db.create_all()

        # ===========================================
        # CONFIGURACIÓN DEL AEROPUERTO
        # ===========================================
        print("✈️  Creando configuración del aeropuerto...")
        config = ConfiguracionAeropuerto(
            nombre='Aeropuerto Internacional de la Ciudad',
            codigo_iata='CIT',
            codigo_icao='MCIT',
            director='Dr. Carlos Mendez',
            direccion='Carretera Federal 123, Km 15',
            codigo_postal='12345',
            municipio='Ciudad de México',
            ciudad='Ciudad de México',
            estado='CDMX',
            pais='México',
            telefono='+52 (55) 1234-5678',
            email='info@aeropuerto-cit.com',
            sitio_web='https://www.aeropuerto-cit.com'
        )
        db.session.add(config)

        # ===========================================
        # AERONAVES (5 registros)
        # ===========================================
        print("🛩️  Creando aeronaves...")
        aeronaves = [
            Aeronave(matricula='XA-ABC', modelo='A320-200', fabricante='Airbus', capacidad=180, tipo_aeronave='Comercial'),
            Aeronave(matricula='XA-DEF', modelo='B737-800', fabricante='Boeing', capacidad=160, tipo_aeronave='Comercial'),
            Aeronave(matricula='XA-GHI', modelo='C208B', fabricante='Cessna', capacidad=12, tipo_aeronave='Privado'),
            Aeronave(matricula='XA-JKL', modelo='A330-300', fabricante='Airbus', capacidad=300, tipo_aeronave='Comercial'),
            Aeronave(matricula='XA-MNO', modelo='B787-9', fabricante='Boeing', capacidad=290, tipo_aeronave='Comercial')
        ]
        db.session.add_all(aeronaves)
        db.session.commit()

        # ===========================================
        # PILOTOS (5 registros)
        # ===========================================
        print("👨‍✈️  Creando pilotos...")
        pilotos = [
            Piloto(nombre='Carlos Ramírez González', licencia='LIC-001', tipo_licencia='ATPL', horas_vuelo=8500, nacionalidad='Mexicana'),
            Piloto(nombre='María López Hernández', licencia='LIC-002', tipo_licencia='CPL', horas_vuelo=4200, nacionalidad='Mexicana'),
            Piloto(nombre='Roberto Silva Martínez', licencia='LIC-003', tipo_licencia='ATPL', horas_vuelo=12000, nacionalidad='Mexicana'),
            Piloto(nombre='Ana García Torres', licencia='LIC-004', tipo_licencia='CPL', horas_vuelo=6800, nacionalidad='Mexicana'),
            Piloto(nombre='Miguel Ángel Cruz', licencia='LIC-005', tipo_licencia='ATPL', horas_vuelo=9500, nacionalidad='Mexicana')
        ]
        db.session.add_all(pilotos)
        db.session.commit()

        # ===========================================
        # VUELOS (5 registros)
        # ===========================================
        print("✈️  Creando vuelos...")
        base_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        vuelos = [
            Vuelo(
                numero_vuelo='AMX101',
                origen='Ciudad de México (MEX)',
                destino='Guadalajara (GDL)',
                fecha_salida=base_date + timedelta(days=1, hours=8, minutes=30),
                fecha_llegada=base_date + timedelta(days=1, hours=10, minutes=0),
                aeronave_id=aeronaves[0].aeronave_id,
                piloto_id=pilotos[0].piloto_id,
                copiloto_id=pilotos[1].piloto_id
            ),
            Vuelo(
                numero_vuelo='VIV202',
                origen='Monterrey (MTY)',
                destino='Cancún (CUN)',
                fecha_salida=base_date + timedelta(days=2, hours=12, minutes=15),
                fecha_llegada=base_date + timedelta(days=2, hours=14, minutes=45),
                aeronave_id=aeronaves[1].aeronave_id,
                piloto_id=pilotos[1].piloto_id,
                copiloto_id=pilotos[2].piloto_id
            ),
            Vuelo(
                numero_vuelo='AER303',
                origen='Tijuana (TIJ)',
                destino='Ciudad de México (MEX)',
                fecha_salida=base_date + timedelta(days=3, hours=6, minutes=0),
                fecha_llegada=base_date + timedelta(days=3, hours=9, minutes=30),
                aeronave_id=aeronaves[2].aeronave_id,
                piloto_id=pilotos[2].piloto_id,
                copiloto_id=pilotos[3].piloto_id
            ),
            Vuelo(
                numero_vuelo='INT404',
                origen='Ciudad de México (MEX)',
                destino='Madrid (MAD)',
                fecha_salida=base_date + timedelta(days=4, hours=22, minutes=0),
                fecha_llegada=base_date + timedelta(days=5, hours=14, minutes=30),
                aeronave_id=aeronaves[3].aeronave_id,
                piloto_id=pilotos[3].piloto_id,
                copiloto_id=pilotos[4].piloto_id
            ),
            Vuelo(
                numero_vuelo='DOM505',
                origen='Guadalajara (GDL)',
                destino='Tijuana (TIJ)',
                fecha_salida=base_date + timedelta(days=5, hours=15, minutes=45),
                fecha_llegada=base_date + timedelta(days=5, hours=17, minutes=15),
                aeronave_id=aeronaves[4].aeronave_id,
                piloto_id=pilotos[4].piloto_id,
                copiloto_id=pilotos[0].piloto_id
            )
        ]
        db.session.add_all(vuelos)
        db.session.commit()

        # ===========================================
        # CONFIRMACIONES (5 registros)
        # ===========================================
        print("🎫 Creando confirmaciones...")
        confirmaciones = [
            Confirmacion(
                vuelo_id=vuelos[0].vuelo_id,
                estado='Confirmado',
                notas='Pasajero VIP, asiento preferencial'
            ),
            Confirmacion(
                vuelo_id=vuelos[1].vuelo_id,
                estado='Pendiente',
                notas='Esperando confirmación de equipaje'
            ),
            Confirmacion(
                vuelo_id=vuelos[2].vuelo_id,
                estado='Confirmado',
                notas='Check-in completado'
            ),
            Confirmacion(
                vuelo_id=vuelos[3].vuelo_id,
                estado='Confirmado',
                notas='Vuelo internacional, documentación verificada'
            ),
            Confirmacion(
                vuelo_id=vuelos[4].vuelo_id,
                estado='Cancelado',
                notas='Cancelado por condiciones climáticas'
            )
        ]
        db.session.add_all(confirmaciones)

        # ===========================================
        # USUARIOS (5 registros)
        # ===========================================
        print("👥 Creando usuarios...")
        
        # Verificar si admin ya existe
        if not Usuario.query.filter_by(username='admin').first():
            admin = Usuario(username='admin', rol='admin')
            admin.set_password('123456')
            db.session.add(admin)
        
        # Crear usuarios adicionales
        usuarios = [
            Usuario(username='operador1', rol='operador'),
            Usuario(username='piloto1', rol='piloto'),
            Usuario(username='invitado1', rol='invitado'),
            Usuario(username='supervisor', rol='admin')
        ]
        
        for usuario in usuarios:
            if not Usuario.query.filter_by(username=usuario.username).first():
                usuario.set_password('123456')
                db.session.add(usuario)

        # ===========================================
        # GUARDAR TODO
        # ===========================================
        db.session.commit()
        
        print("\n" + "="*50)
        print("✅ SEED COMPLETADO EXITOSAMENTE")
        print("="*50)
        print(f"📊 Resumen de datos creados:")
        print(f"   🛩️  Aeronaves: {Aeronave.query.count()}")
        print(f"   👨‍✈️  Pilotos: {Piloto.query.count()}")
        print(f"   ✈️  Vuelos: {Vuelo.query.count()}")
        print(f"   🎫 Confirmaciones: {Confirmacion.query.count()}")
        print(f"   👥 Usuarios: {Usuario.query.count()}")
        print(f"   ⚙️  Configuración: {ConfiguracionAeropuerto.query.count()}")
        print("\n🔑 Credenciales de acceso:")
        print("   Usuario: admin")
        print("   Contraseña: 123456")
        print("\n🌐 Acceder en: http://127.0.0.1:5000")
        print("="*50)

if __name__ == '__main__':
    seed_data()