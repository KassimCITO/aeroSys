<<<<<<< HEAD
from app import app, db

with app.app_context():
    # Eliminar todas las tablas
    db.drop_all()
    # Crear todas las tablas nuevamente
    db.create_all()
    
    # Crear usuario admin
    from models import Usuario
    admin = Usuario(username='admin', rol='admin')
    admin.set_password('123456')
    db.session.add(admin)
    db.session.commit()
=======
from app import app, db

with app.app_context():
    # Eliminar todas las tablas
    db.drop_all()
    # Crear todas las tablas nuevamente
    db.create_all()
    
    # Crear usuario admin
    from models import Usuario
    admin = Usuario(username='admin', rol='admin')
    admin.set_password('123456')
    db.session.add(admin)
    db.session.commit()
>>>>>>> 348e468 (Actualización de archivos y carpetas)
    print('Base de datos reiniciada y usuario admin creado')