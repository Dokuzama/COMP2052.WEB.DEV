from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_loaded, identity_changed, AnonymousIdentity
from forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_roles'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

principal = Principal(app)

admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

class Usuario(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

usuarios = {
    "admin": Usuario(id=1, username="admin", password="admin123", role="admin"),
    "usuario": Usuario(id=2, username="usuario", password="usuario123", role="user")
}

@login_manager.user_loader
def load_user(user_id):
    for usuario in usuarios.values():
        if str(usuario.id) == user_id:
            return usuario
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'role'):
        identity.provides.add(RoleNeed(current_user.role))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = usuarios.get(form.username.data)
        if usuario and check_password_hash(usuario.password_hash, form.password.data):
            login_user(usuario)
            identity_changed.send(app, identity=Identity(usuario.id))
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for("index"))
        else:
            flash("Usuario o contraseña incorrectos.", "danger")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    flash("Sesión cerrada.", "success")
    return redirect(url_for("login"))

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/index")
@login_required
def index():
    return render_template("index.html")

@app.route("/admin")
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return render_template("admin.html")

@app.route("/user")
@login_required
@user_permission.require(http_exception=403)
def user():
    return render_template("user.html")

if __name__ == "__main__":
    app.run(debug=True)
