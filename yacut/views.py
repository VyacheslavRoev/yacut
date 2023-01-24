import logging

from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import YacutForm
from .models import URLMap
from .settings import configure_logging
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    configure_logging()
    logging.info('Приложение запущено!')
    form = YacutForm()
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        if URLMap.query.filter_by(short=short).first() is not None:
            flash(f'Имя {short} уже занято!', 'short_error_message')
            return render_template('main.html', form=form)
        try:
            urlmap = URLMap(
                original=form.original_link.data,
                short=short
            )
        except Exception:
            logging.error('Не получилось создать экземпляр класса URLMap.')
            return render_template('500.html')
        # Вот всё, что я смог накопать в документации в плане обработки ошибок при записи в БД
        # Это нормальный вариант или стоит еще поковыряться?
        with app.app_context():
            try:
                db.session.add(urlmap)
            except Exception:
                db.session.rollback()
                logging.error('Не получилось записать данные в базу!')
                return render_template('500.html')
            else:
                db.session.commit()
                flash(url_for('unique_short', short=short, _external=True), 'short_message')
                logging.info('Данные успешно записаны в базу.')
    return render_template('main.html', form=form)


@app.route('/<string:short>')
def unique_short(short):
    return redirect(URLMap.query.filter_by(short=short).first_or_404().original)
