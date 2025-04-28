from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(message="El nombre de usuario es obligatorio.")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="La contraseña es obligatoria.")])
    submit = SubmitField('Iniciar sesión')
