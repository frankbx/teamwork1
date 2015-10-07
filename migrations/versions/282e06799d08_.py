"""empty message

Revision ID: 282e06799d08
Revises: 52da5bfaf044
Create Date: 2015-09-28 12:51:47.139000

"""

# revision identifiers, used by Alembic.
revision = '282e06799d08'
down_revision = '52da5bfaf044'

from app.models import Role, User, db


def upgrade():
    admin_role = Role(role_name='admin')
    user_role = Role(role_name='user')
    db.session.add(admin_role)
    db.session.add(user_role)
    db.session.commit()
    admin_user = User(first_name='Xiang', last_name='Bao', sso='305012589', role_id=admin_role.id,
                      email='xiang.bao@med.ge.com')
    admin_user.password = '305012589'
    db.session.add(admin_user)
    db.session.commit()


def downgrade():
    pass
