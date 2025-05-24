from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])

def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe.')
            return redirect(url_for('auth.register'))
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Regsitro realizado! Faça Login.')
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash('Credencias inválidas.')
            return redirect(url_for('auth.login'))
        login_user(user, remember=remember)
        return redirect(url_for('main.index'))
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))