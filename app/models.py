from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from . import login_manager
from app import db


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(10), unique=True, default='user')
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.role_name

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    sso = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    def __repr__(self):
        return '<User %r, %r>' % (self.last_name, self.first_name)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Machine(db.Model):
    __tablename__ = 'machines'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), nullable=False)
    sn = db.Column(db.String(20), nullable=False)
    power_input = db.Column(db.String(100))
    drive_gas = db.Column(db.String(100))
    acgo = db.Column(db.String(100))
    aux_o2 = db.Column(db.String(100))
    aux_gas = db.Column(db.String(100))
    pipeline = db.Column(db.String(100))
    cylinder = db.Column(db.String(100))
    display_unit = db.Column(db.String(100))
    pmb = db.Column(db.String(100))
    acb = db.Column(db.String(100))
    fib = db.Column(db.String(100))
    sib = db.Column(db.String(100))
    vent_engine = db.Column(db.String(100))
    breathing_system = db.Column(db.String(100))
    agss = db.Column(db.String(100))
    ac_outlet = db.Column(db.String(100))
    transformer = db.Column(db.String(100))
    sw = db.Column(db.String(100))
    bag_arm = db.Column(db.String(100))
    others = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime)
    last_updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    last_updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Machine: %r, SN: %r>' % (self.product_name, self.sn)

    def save(self):
        db.session.add(self)
        db.session.commit()
