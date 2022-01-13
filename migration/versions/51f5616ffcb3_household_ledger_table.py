"""financial_ledger_table

Revision ID: 51f5616ffcb3
Revises: 84d2d97d39a9
Create Date: 2022-01-12 15:06:44.934031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51f5616ffcb3'
down_revision = '8b6d2543dcbb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('household_ledgers',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('transfer_id', sa.Integer(), nullable=False),
        sa.Column('memo', sa.String(length=100), nullable=False),
        sa.Column('price', sa.Numeric(14,2), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('is_delete', sa.Boolean(), default=False, nullable=False),
        sa.UniqueConstraint('name'),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('household_ledgers')
