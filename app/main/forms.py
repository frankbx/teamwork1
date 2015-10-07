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
