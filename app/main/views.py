from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import sent_email
from flask_login import login_required


@main.route('/', methods=['POST', 'GET'])
@login_required
def index():
    print(session.items())
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role_id=3)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            if current_app.config['FLASK_ADMIN']:
                sent_email(current_app.config['FLASK_ADMIN'], 'New User', 'mail/new_user', user=user.username)
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    print(session.items())
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'),
                           known=session.get('known', False))
