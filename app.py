from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Crear tabla si no existe
def init_db():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        nombre = request.form["nombre"]
        edad = request.form["edad"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO pacientes (nombre, edad) VALUES (?, ?)",
            (nombre, edad)
        )

        conn.commit()
        conn.close()

        return f"Paciente registrado correctamente: {nombre}"
    return render_template("index.html")

@app.route("/pacientes")
def pacientes():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")

    datos = cursor.fetchall()

    conn.close()

    return render_template("pacientes.html", pacientes=datos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)