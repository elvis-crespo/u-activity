from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from forms import RegistrationForm, LoginForm

# Configuración básica de la app Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Cambia esto por una clave secreta real
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirigir a esta vista si el usuario no está autenticado

# Modelo de usuario
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Cargar el usuario para la sesión de login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Ruta para el registro de usuarios (sin necesidad de estar logueado)
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('apartment_rental_template'))

    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Ese nombre de usuario ya está en uso. Elige otro.', 'danger')
            return redirect(url_for('register'))

        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Ese correo ya está en uso. Elige otro.', 'danger')
            return redirect(url_for('register'))

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash('Tu cuenta ha sido creada! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Registro', form=form)

# Ruta para el login de usuarios
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('apartment_rental_template'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Has iniciado sesión con éxito.', 'success')
            return redirect(url_for('apartment_rental_template'))  # Redirigir a "ApartmentRentalTemplate"
        else:
            flash('Inicio de sesión fallido. Verifica tu correo y contraseña.', 'danger')
    
    return render_template('login.html', title='Iniciar Sesión', form=form)

# Ruta para cerrar sesión
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

# Ruta principal (ApartmentRentalTemplate)
@app.route("/")
@login_required
def apartment_rental_template():
    return render_template('apartment_rental.html', user_name=current_user.username)

# Iniciar la app Flask
if __name__ == '__main__':
    app.run(debug=True)