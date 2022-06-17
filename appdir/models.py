from datetime import datetime
from appdir import db, login_manager
from flask_login import UserMixin
import enum


@login_manager.user_loader
def load_user(user_username):
    return User.query.get(user_username)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    sensors = db.relationship('Sensor', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class SensorTypes(enum.Enum):
    TEMPERATURE = 'temperature'
    HUMIDITY = 'humidity'
    PRESSURE = 'pressure'
    LUMINOSITY = 'luminosity'


class Sensor(db.Model, UserMixin):
    model_no = db.Column(db.String(30), nullable=False, primary_key=True)
    type = db.Column(db.Enum(SensorTypes), nullable=False)
    desc = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Float(precision=6), nullable=True)
    longitude = db.Column(db.Float(precision=6), nullable=True)
    value = db.Column(db.Float(precision=6), nullable=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.model_no} {self.type} {self.latitude} {self.longitude} {self.value}"