from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import os


class UnlockedAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        if "isolation_level" not in options:
            options["isolation_level"] = "READ COMMITTED"
        return super(UnlockedAlchemy, self).apply_driver_hacks(app, info, options)


app = Flask(__name__)
mysql = MySQL()
db = UnlockedAlchemy()


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

    db_uri = 'mysql+mysqlconnector://'
    db_uri += "root" + ':'
    db_uri += "root" + '@'
    db_uri += "db" + ':3306/'
    db_uri += "test"

    # Override finalize so that NUll DB values do not print in jinja as the string "None"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri  # 'mysql+mysqlconnector://' + root:example@db:3306/carcity'
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 499
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    mysql.init_app(app)
    db.init_app(app)

    # register blueprints
    from routes import main_blueprint
    app.register_blueprint(main_blueprint)
    app.run(host='0.0.0.0', debug=True)
