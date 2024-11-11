from flask import Flask, render_template, request, redirect, url_for, flash
from config import init_app

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configurar la base de datos
mysql = init_app(app)

# Ruta para mostrar todos los usuarios
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

# Ruta para agregar un nuevo usuario
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        flash('Usuario agregado exitosamente')
        return redirect(url_for('index'))
    return render_template('add_user.html')

# Ruta para editar el correo electrónico de un usuario
@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        email = request.form['email']
        cursor.execute("UPDATE users SET email=%s WHERE id=%s", (email, id))
        mysql.connection.commit()
        flash('Correo actualizado exitosamente')
        return redirect(url_for('index'))
    
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    return render_template('edit_user.html', user=user)

# Ruta para eliminar un usuario
@app.route('/delete_user/<int:id>', methods=['GET'])
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    flash('Usuario eliminado exitosamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)