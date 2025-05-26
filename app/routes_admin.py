from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import Ticket, User

admin = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(f):
    """Decorator que bloqueia acesso senão for admin"""
    def wrap(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap


@admin.route('/')
@login_required # Só permite acesso se o usuário estiver logado.
@admin_required
def dashboard():
    tickets = Ticket.query.order_by(Ticket.id.desc()).all()
    users = User.query.order_by(User.username).all() # Carrea todos os usuários
    return render_template('admin_dashboard.html', tickets=tickets)


# Editar status do chamado aberto em questão.
@admin.route('/edit/<int:ticket_id>', methods=['GET', 'POST'])
@login_required
def edit_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    if request.method == 'POST':
        ticket.title        = request.form['title']
        ticket.description  = request.form['description']
        ticket.status       = request.form['status']
        db.session.commit()
        flash('Chamado atualizado com sucesso.')
        return redirect(url_for('admin.dashboard'))
    return render_template('edit_ticket.html', ticket=ticket)

# Deletar chamado aberto em questão
@admin.route('/delete/<int:ticket_id>', methods=['POST'])
@login_required
def delete_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash('Chamado excluído.')
    return redirect(url_for('admin.dashboard'))

@admin.route('/toggle_admin/<int:user_id>', methods='POST')
@login_required
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user.id)
    if user.id == current_user.id:
        flash('Você não pode alterar sua própria permissão.')
    else:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash(f'Permissão de {user.username} atualizada')
    return redirect(url_for('admin.dashboard'))