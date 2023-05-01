from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()


if __name__ == '__main__':

    app.config['SECRET_KEY'] = 'dfasfsdvfsfd34ds2dfs'
    app.config["SECURITY_PASSWORD_SALT"] = '525LAIDLAW2048899069'
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.url_map.strict_slashes = False

    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'test'

    mysql.init_app(app)

    # register blueprints
    from routes import main_blueprint
    app.register_blueprint(main_blueprint)
    app.run(host='0.0.0.0', debug=True)
