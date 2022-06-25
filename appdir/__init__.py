import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '__RANDOM_KEY__'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')

db = SQLAlchemy(app)


def split_func(strn):
    t = f'{strn}'
    return t.split()


app.jinja_env.globals.update(split_func=split_func)

from appdir import routes
