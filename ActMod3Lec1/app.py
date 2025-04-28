from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_login'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class Usuario(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

usuarios = {
    "admin": Usuario(id=1, username="admin", password="admin123", role="admin")
}

@login_manager.user_loader
def load_user(user_id):
    for usuario in usuarios.values():
        if str(usuario.id) == user_id:
            return usuario
    return None

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = usuarios.get(form.username.data)
        if usuario and check_password_hash(usuario.password_hash, form.password.data):
            login_user(usuario)
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for("protegido"))
        else:
            flash("Usuario o contraseña incorrectos.", "danger")
    return render_template("login.html", form=form)

@app.route("/protegido")
@login_required
def protegido():
    return render_template("protegido.html", nombre=current_user.username)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
