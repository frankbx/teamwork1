"""empty message

Revision ID: 56da710fe1aa
Revises: 3e908863b911
Create Date: 2015-10-08 13:38:16.152000

"""

# revision identifiers, used by Alembic.
revision = '56da710fe1aa'
down_revision = '3e908863b911'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('machines',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_name', sa.String(length=20), nullable=False),
                    sa.Column('sn', sa.String(length=20), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('last_updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('tracking_records',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=20), nullable=False),
                    sa.Column('pn', sa.String(length=20), nullable=False),
                    sa.Column('revision', sa.Integer(), nullable=False),
                    sa.Column('is_latest', sa.Boolean(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('machine_id', sa.Integer(), nullable=True),
                    # sa.ForeignKeyConstraint(['machine_id'], ['machines.id'], ),
                    # sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # op.add_column(u'products', sa.Column('is_active', sa.Boolean(), nullable=False, default=True))
    # op.add_column(u'tracking_items', sa.Column('is_active', sa.Boolean(), nullable=False, default=True))
    # op.add_column(u'tracking_items', sa.Column('pn', sa.String(length=20)))
    # op.alter_column(u'users', 'email',
    #            existing_type=sa.VARCHAR(length=64),
    #            nullable=True)
    # op.alter_column(u'users', 'password_hash',
    #            existing_type=sa.VARCHAR(length=128),
    #            nullable=True)
    # op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'users', type_='foreignkey')
    # op.alter_column(u'users', 'password_hash',
    #            existing_type=sa.VARCHAR(length=128),
    #            nullable=False)
    # op.alter_column(u'users', 'email',
    #            existing_type=sa.VARCHAR(length=64),
    #            nullable=False)
    op.drop_column(u'tracking_items', 'pn')
    op.drop_column(u'tracking_items', 'is_active')
    op.drop_column(u'products', 'is_active')
    op.drop_table('tracking_records')
    op.drop_table('machines')
    ### end Alembic commands ###
