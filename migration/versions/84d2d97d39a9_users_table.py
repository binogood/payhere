"""users_table

Revision ID: 84d2d97d39a9
Revises: 
Create Date: 2022-01-12 15:06:26.539174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84d2d97d39a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False),
        sa.Column('password', sa.String(length=130), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.UniqueConstraint('email'),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('users')
