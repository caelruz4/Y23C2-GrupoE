
from cs50 import SQL
from flask_session import Session
from flask import Flask, flash, redirect, render_template, request, session, jsonify, flash

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = '12345'

Session(app)

db = SQL("sqlite:///tasks.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    user = session.get("user", None)

    if user is None:
        return redirect("/register")

    tareas = db.execute("SELECT id, descripcion, completed FROM tasks WHERE user_id = :user_id", user_id=session["user_id"])
    print(tareas)
    return render_template('index.html', tareas=tareas)

@app.route('/register', methods=["GET", "POST"] )
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if password != confirm:
            return "Error"

        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                   username=username, password=password)

        session["user"] = username
        #
        user_id = db.execute("SELECT id FROM users WHERE username = :username", username=username)
        session["user_id"] = user_id[0]["id"]
        return redirect("/")

@app.route('/agregar', methods=["POST"])
def agregar():
    user = session.get("user", None)
    if user is None:
        return redirect("/register")
    description = request.form.get("description")
    # Insertar la nueva tarea en la base de datos
    db.execute("INSERT INTO tasks (user_id, descripcion) VALUES (:user_id, :description)",
               user_id=session["user_id"], description=description)
    return redirect("/")

@app.route('/borrar/<int:id>', methods=['POST'])
def borrar(id):
    db.execute("Delete from tasks where id = ?",id)
    return redirect("/")

@app.route('/completar/<int:id>', methods=['POST'])
def completar(id):
    db.execute("UPDATE tasks SET completed = 1 WHERE id = :task_id AND user_id = :user_id", task_id=id, user_id=session["user_id"])
    return redirect("/")
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
