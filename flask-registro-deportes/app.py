from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///registros.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Registro
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        deporte = request.form.get('deporte')

        if not nombre:
            return render_template('error.html', mensaje = "No ingresaste un nombre")
        if not deporte:
            return render_template('error.html', mensaje = "No ingresaste un deporte")

        db.execute("INSERT INTO personas (nombre, deporte) VALUES(?, ?)", nombre, deporte)
        return redirect('/')
    # Si el metodo es get
    return render_template('register.html')

@app.route('/ver-registros', methods=['GET', 'POST'])
def registros():
    personas = db.execute("SELECT * FROM personas")
    print(personas)
    return render_template('registrados.html', personas = personas)

@app.route('/borrar/<int:id>', methods=['POST'])
def borrar(id):
    db.execute("Delete from personas where id = ?",id)
    return redirect("/ver-registros")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
