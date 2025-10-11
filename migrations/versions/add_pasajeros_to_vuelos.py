"""add pasajeros to vuelos

Revision ID: add_pasajeros
Revises: add_aeropuerto_id
Create Date: 2025-10-11 15:25:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_pasajeros'
down_revision = 'add_aeropuerto_id'
branch_labels = None
depends_on = None


def upgrade():
    # Agregar campo pasajeros a Vuelos
    with op.batch_alter_table('Vuelos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pasajeros', sa.Text(), nullable=True))


def downgrade():
    # Eliminar campo pasajeros de Vuelos
    with op.batch_alter_table('Vuelos', schema=None) as batch_op:
        batch_op.drop_column('pasajeros')
