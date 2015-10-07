"""empty message

Revision ID: 52da5bfaf044
Revises: None
Create Date: 2015-09-28 11:16:19.935000

"""

# revision identifiers, used by Alembic.
revision = '52da5bfaf044'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('roles',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('role_name', sa.String(10), unique=True, default='user'))
    op.create_table('users',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('sso', sa.Integer, unique=True, nullable=False),
                    sa.Column('first_name', sa.String(20), nullable=False),
                    sa.Column('last_name', sa.String(20), nullable=False),
                    sa.Column('role_id', sa.Integer),
                    sa.Column('email', sa.String(64), unique=True, nullable=False),
                    sa.Column('password_hash', sa.String(128), nullable=False))


def downgrade():
    op.drop_table('users')
    op.drop_table('roles')
