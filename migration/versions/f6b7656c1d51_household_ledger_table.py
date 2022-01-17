"""household_ledger_table

Revision ID: f6b7656c1d51
Revises: 84d2d97d39a9
Create Date: 2022-01-15 14:29:27.944357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6b7656c1d51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('household_ledger',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('memo', sa.String(length=100), nullable=False),
        sa.Column('transfer', sa.String(length=20), nullable=False),
        sa.Column('price', sa.Numeric(14, 2), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('is_delete', sa.Boolean(), default=False, nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='cascade'),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('household_ledger')