"""Region, district added

Revision ID: e29c437658ad
Revises: 45ac5e83e767
Create Date: 2024-11-25 23:41:24.077522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e29c437658ad'
down_revision: Union[str, None] = '45ac5e83e767'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('district',
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('region',
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('region')
    op.drop_table('district')
    # ### end Alembic commands ###