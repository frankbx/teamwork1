from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from ..models import User, Role


class LoginForm(Form):
    sso = StringField('SSO', validators=[DataRequired(), Length(9)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class UserForm(Form):
    sso = StringField('SSO', validators=[DataRequired(), Length(9, 9)])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', coerce=int)
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message="Passwords must "
                                                                                                  "match.")])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Create User")

    def validate_sso(self, sso):
        if User.query.filter_by(sso=sso.data).first() is not None:
            raise ValidationError('SSO already exists')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.role_name) for role in Role.query.all()]


class MachineForm(Form):
    product_name = StringField('Product', validators=[DataRequired()])
    sn = StringField('SN', validators=[DataRequired()])
    sw = StringField('SW Versioin', validators=[DataRequired()])
    power_input = StringField('Power Input', validators=[DataRequired()])
    drive_gas = StringField('Drive Gas', validators=[DataRequired()])
    acgo = StringField('ACGO', validators=[DataRequired()])
    aux_o2 = StringField('Aux O2', validators=[DataRequired()])
    aux_gas = StringField('Aux Gas', validators=[DataRequired()])
    pipeline = StringField('Pipeline', validators=[DataRequired()])
    cylinder = StringField('Cylinder', validators=[DataRequired()])
    display_unit = StringField('Display Unit/Board', validators=[DataRequired()])
    pmb = StringField('Power Management Board', validators=[DataRequired()])
    acb = StringField('Anes Control Board', validators=[DataRequired()])
    fib = StringField('FIB', validators=[DataRequired()])
    sib = StringField('SIB', validators=[DataRequired()])
    vent_engine = StringField('Vent Engine', validators=[DataRequired()])
    breathing_system = StringField('Breathing System', validators=[DataRequired()])
    agss = StringField('AGSS', validators=[DataRequired()])
    ac_outlet = StringField('AC Outlet', validators=[DataRequired()])
    transformer = StringField('Transformer', validators=[DataRequired()])
    bag_arm = StringField('Bag Arm', validators=[DataRequired()])
    others = StringField('Others', validators=[DataRequired()])
    submit = SubmitField("Create")
