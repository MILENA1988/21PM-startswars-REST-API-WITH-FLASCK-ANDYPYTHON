"""empty message

Revision ID: bce91e2653bf
Revises: d279afdc265a
Create Date: 2021-03-04 17:14:37.369477

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bce91e2653bf'
down_revision = 'd279afdc265a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='favoritos')
    op.drop_column('favoritos', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favoritos', sa.Column('name', mysql.VARCHAR(length=200), nullable=True))
    op.create_index('name', 'favoritos', ['name'], unique=True)
    # ### end Alembic commands ###
