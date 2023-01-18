from . import app, db
from flask import render_template, flash, redirect, url_for
from .forms import YacutForm
from .models import URLMap

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        urlmap = URLMap(
            original=form.original_link.data,
            short=form.custom_id.data
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(url_for('unique_short', short=form.custom_id.data, _external=True))

    return render_template('main.html', form=form)

@app.route('/<string:short>')
def unique_short(short):
    return redirect(URLMap.query.filter_by(short=short))
