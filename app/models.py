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
        return '<User %r>' % (self.last_name, self.first_name)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200))
    tracking_items = db.relationship('TrackingItem', backref='product')
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return '<Product %r>' % self.product_name


class TrackingItem(db.Model):
    __tablename__ = 'tracking_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pn = db.Column(db.String(20), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return '<Tracking Item %r>' % self.name


class Machine(db.Model):
    __tablename__ = 'machines'
    id = db.Column(db.Integer, primary_key=True)
    sn = db.Column(db.String(20), nullable=False)
    tracking_records = db.relationship('TrackingRecord', backref='machine')
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime)
    last_updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return '<Machine %r>' % self.sn


class TrackingRecord(db.Model):
    __tablename__ = 'tracking_records'
    id = db.Column(db.Integer, primary_key=True)
    revision = db.Column(db.Integer, nullable=False)
