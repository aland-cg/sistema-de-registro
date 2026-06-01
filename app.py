# Importar herramientas necesarias de Flask
from flask import Flask, render_template, request
# Importar SQLite para guardar datos
import sqlite3
#importar fecha y hora
from datetime import datetime

# Crear instancia principal de la aplicación Flask
app = Flask(__name__)
#inicializa la base de datos
def init_db():
# crea conexion con la base de datos
    conn = sqlite3.connect("database.db")
#ejecuta comandos de sql
    cursor = conn.cursor()
# Crear tabla principal de pacientes si aún no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER,
    ta TEXT,
    fc INTEGER,
    spo2 INTEGER,
    temp REAL,
    glucosa INTEGER,
    fecha TEXT,
    hora TEXT               
);
    """)
#sirve para guardar cambios 
    conn.commit()
#cierra la conexion lo que evita errores de escritura una vez que se capturan los datos
    conn.close()

init_db()

# Ruta principal para registrar pacientes
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        
        paciente = {
        "nombre": request.form["nombre"],
        "edad": request.form["edad"],
        "ta": request.form["ta"],
        "fc": request.form["fc"],
        "spo2": request.form["spo2"],
        "temp": request.form["temp"],
        "glucosa": request.form["glucosa"],
        

    }
        #consulta la fecha y hora y la integra al campo de la DB
        ahora = datetime.now()

        fecha = ahora.strftime("%Y-%m-%d")
        hora = ahora.strftime("%H:%M:%S")

        # Validaciones

        edad = int(paciente["edad"])

        if edad < 0 or edad > 120:
            return "Error: Edad fuera de rango permitido."

        fc = int(paciente["fc"])

        if fc < 20 or fc > 250:
            return "Error: Frecuencia cardiaca fuera de rango permitido."

        spo2 = int(paciente["spo2"])

        if spo2 < 50 or spo2 > 100:
            return "Error: Saturación fuera de rango permitido."

        glucosa = int(paciente["glucosa"])

        if glucosa < 20 or glucosa > 800:
            return "Error: Glucosa fuera de rango permitido."
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
# Insertar datos clínicos del paciente en SQLite
        cursor.execute(
    """
    INSERT INTO pacientes
    (nombre, edad, ta, fc, spo2, temp, glucosa, fecha, hora)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        paciente["nombre"],
        paciente["edad"],
        paciente["ta"],
        paciente["fc"],
        paciente["spo2"],
        paciente["temp"],
        paciente["glucosa"],
        fecha,
        hora
    )
)

        conn.commit()
        conn.close()
#devuelven respuestas al usuario
        return f"Paciente registrado correctamente: {paciente['nombre']}"
#muestra el formilario html
    return render_template("index.html")
#consulta registros guardados
#Iniciar servidor Flask en modo desarrollo
@app.route("/pacientes")
def pacientes():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")

    datos = cursor.fetchall()

    conn.close()

    return render_template("pacientes.html", pacientes=datos)
## Iniciar servidor Flask en modo desarrollo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)