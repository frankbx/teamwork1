# -- coding: UTF-8 --
from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import login_user, logout_user, login_required

from app.main import main
from .forms import LoginForm, UserForm, MachineForm
from ..models import User, Machine


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
    users = User.query.all()

    return render_template('manage_users.html', users=users)


@main.route('/manage_machines', methods=['GET', 'POST'])
@login_required
def manage_machines():
    machines = Machine.query.all()

    return render_template('manage_machines.html', machines=machines)


@main.route('/user/new', methods=['GET', 'POST'])
@login_required
def new_user():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user = User()
        user.sso = user_form.sso.data
        user.first_name = user_form.first_name.data
        user.last_name = user_form.last_name.data
        user.email = user_form.email.data
        user.password = user_form.password.data
        user.role_id = user_form.role.data
        user.save()
        return redirect(url_for('main.manage_users'))
    return render_template('new_user.html', user_form=user_form)


@main.route('/machine/new', methods=['GET', 'POST'])
@login_required
def new_machine():
    form = MachineForm()
    if form.validate_on_submit():
        machine = Machine()
        # machine.product_name = form.product_name.data
        # machine.description = form.description.data
        # machine.is_active = form.is_active.data
        machine = form.populate_obj()
        machine.save()
        flash('New Machine created successfully.')
        return redirect(url_for('main.manage_machines'))
    return render_template('new_machine.html', form=form)
