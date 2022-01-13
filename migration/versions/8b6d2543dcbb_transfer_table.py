"""transfer_table

Revision ID: 8b6d2543dcbb
Revises: 51f5616ffcb3
Create Date: 2022-01-12 15:07:09.055904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b6d2543dcbb'
down_revision = '84d2d97d39a9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('transfer',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(10), nullable=False),
        sa.UniqueConstraint('name'),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('fransfer')
