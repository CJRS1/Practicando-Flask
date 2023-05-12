"""migracion inicial

Revision ID: 71823564c970
Revises: 
Create Date: 2023-05-12 13:47:42.081752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71823564c970'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('nombre', sa.String(length=45), nullable=False),
    sa.Column('correo', sa.String(length=45), nullable=False),
    sa.Column('telefono', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###