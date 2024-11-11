from flask_mysqldb import MySQL

def init_app(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '1967188'
    app.config['MYSQL_DB'] = 'flask_app_db'
    mysql = MySQL(app)
    return mysql