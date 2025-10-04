"""add Observaciones to Vuelos

Revision ID: 5f1b2c3d4e5f
Revises: d08f6bbd878e
Create Date: 2025-10-03 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f1b2c3d4e5f'
down_revision = 'd08f6bbd878e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Vuelos', sa.Column('observaciones', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('Vuelos', 'observaciones')


