from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Para mostrar mensajes flash

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/init_db')
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS asistentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            nombres TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            edad INTEGER NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    return 'Base de datos y tabla de asistentes creadas!'

@app.route('/')
def index():
    return render_template('registro.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    tipo = request.form['tipo']
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    edad = request.form['edad']
    email = request.form['email']
    password = request.form['password']

    # Validación en el servidor
    if not tipo or not nombres or not apellidos or not edad or not email or not password:
        flash('Todos los campos son obligatorios', 'error')
        return redirect(url_for('index'))

    if int(edad) < 18:
        flash('Debes tener al menos 18 años', 'error')
        return redirect(url_for('index'))

    if len(password) < 6:
        flash('La contraseña debe tener al menos 6 caracteres', 'error')
        return redirect(url_for('index'))

    conn = get_db_connection()
    conn.execute('INSERT INTO asistentes (tipo, nombres, apellidos, edad, email, password) VALUES (?, ?, ?, ?, ?, ?)',
                 (tipo, nombres, apellidos, edad, email, password))
    conn.commit()
    conn.close()

    flash('Registro exitoso', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
