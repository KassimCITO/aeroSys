"""add imagen to Aeronaves

Revision ID: 7a8b9c0d1e2f
Revises: 5f1b2c3d4e5f
Create Date: 2025-10-03 00:10:00.000000
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a8b9c0d1e2f'
down_revision = '5f1b2c3d4e5f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Aeronaves', sa.Column('imagen', sa.String(length=255), nullable=True))


def downgrade():
    op.drop_column('Aeronaves', 'imagen')


