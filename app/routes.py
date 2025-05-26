from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import Ticket
from app import db

main = Blueprint('main', __name__)


@main.route('/')
def  index():
    tickets = Ticket.query.order_by(Ticket.id.desc()).all()
    return render_template('index.html', tickets=tickets)


@main.route('/create', methods=['GET', 'POST'])

def create_ticket():
@login_required

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']
        new = Ticket(title=title, description=desc)
        new = Ticket(
            title=title,
            description=desc,
            user_id=current_user.id # Vincula o Ticket ao usuário logado
        )
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_ticket.html')


