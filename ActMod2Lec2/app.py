from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistroForm

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_formularios'

@app.route("/registro", methods=["GET", "POST"])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        flash("Usuario registrado exitosamente.", "success")
        return redirect(url_for("registro"))
    return render_template("registro.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
