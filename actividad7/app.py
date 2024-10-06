# # from flask import Flask, render_template

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('inicio.html', user_name="Elvis")

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=False, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Ese nombre de usuario ya está en uso. Elige otro.', 'danger')
            return redirect(url_for('register'))
        existing_user = User.query.filter_by(username=form.email.data).first()
        if existing_user:
            flash('Email ya está en uso. Elige otro.', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()  
        flash('Tu cuenta ha sido creada! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))  
    return render_template('register.html', title='Register', form=form)

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
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     print(f"Usuario encontrado: {user}")  
        
    #     # Verifica si el usuario existe y la contraseña coincide
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user)
    #         # return redirect('/')  # Redirige a la página principal
    #         return redirect(url_for('/'))  # Esto redirige a la función apartment_rental_template

    #     else:
    #         print("Login failed")  # Debugging
    #         flash('Login Unsuccessful. Please check email ad password', 'danger')
    # return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/")
@login_required
def apartment_rental_template():
    return render_template('inicio.html', user_name="current_user.username")
    # return render_template('inicio.html')

# Nueva ruta para mostrar todos los usuarios
@app.route("/users")
# @login_required
def all_users():
    users = User.query.all()  # Recupera todos los usuarios de la base de datos
    return render_template('users.html', users=users)    


if __name__ == '__main__':
    app.run(debug=True)

