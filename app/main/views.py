# -- coding: UTF-8 --
from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import login_user, logout_user, login_required

from app.main import main
from .forms import LoginForm, UserForm
from ..models import User


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/admin')
@login_required
def admin():
    return render_template('admin.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(sso=form.sso.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@main.route('/manage_users', methods=['GET', 'POST'])
@login_required
def manage_users():
    user_form = UserForm()
    if user_form.validate_on_submit():
        # user = User.query.filter_by(sso=user_form.sso.data).first()
        # if user is not None:
        #     flash('The user already exists!')
        #     # return redirect(url_for('main.manage_users'))
        # else:
        #     pass
        return redirect(url_for('main.index'))

    return render_template('manage_users.html', user_form=user_form)
