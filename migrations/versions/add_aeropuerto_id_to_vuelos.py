"""add aeropuerto_id to vuelos and activo to configuracion_aeropuerto

Revision ID: add_aeropuerto_id
Revises: d08f6bbd878e
Create Date: 2025-10-11 15:05:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_aeropuerto_id'
down_revision = '4d2d59090924'
branch_labels = None
depends_on = None


def upgrade():
    # Agregar campo activo a configuracion_aeropuerto
    with op.batch_alter_table('configuracion_aeropuerto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('activo', sa.Boolean(), nullable=True, server_default='1'))
    
    # Agregar campo aeropuerto_id a Vuelos
    with op.batch_alter_table('Vuelos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('aeropuerto_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_vuelos_aeropuerto', 'configuracion_aeropuerto', ['aeropuerto_id'], ['id'])
    
    # Asignar el primer aeropuerto a todos los vuelos existentes
    op.execute("""
        UPDATE Vuelos 
        SET aeropuerto_id = (SELECT id FROM configuracion_aeropuerto ORDER BY id LIMIT 1)
        WHERE aeropuerto_id IS NULL
    """)


def downgrade():
    # Eliminar campo aeropuerto_id de Vuelos
    with op.batch_alter_table('Vuelos', schema=None) as batch_op:
        batch_op.drop_constraint('fk_vuelos_aeropuerto', type_='foreignkey')
        batch_op.drop_column('aeropuerto_id')
    
    # Eliminar campo activo de configuracion_aeropuerto
    with op.batch_alter_table('configuracion_aeropuerto', schema=None) as batch_op:
        batch_op.drop_column('activo')
