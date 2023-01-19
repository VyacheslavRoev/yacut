from . import app, db
from flask import render_template, flash, redirect, url_for, abort
from .forms import YacutForm
from .models import URLMap
from .utils import get_unique_short_id

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        if URLMap.query.filter_by(short=short).first() is not None:
            flash('Такой адрес уже существует', 'short_error_message')
            return render_template('main.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(url_for('unique_short', short=short, _external=True), 'short_message')

    return render_template('main.html', form=form)

@app.route('/<string:short>')
def unique_short(short):
    return redirect(URLMap.query.filter_by(short=short).first_or_404())
