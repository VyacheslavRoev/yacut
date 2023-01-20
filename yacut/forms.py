from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class YacutForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(require_tld=True, message='Необходимо ввести URL-адрес'),
            Length(1, 256)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Regexp(
                r'^[A-Za-z0-9]+$',
                message='Можно использовать только латинские буквы и цифры от 0 до 9'
            ),
            Length(1, 16),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
