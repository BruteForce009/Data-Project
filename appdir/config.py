import os


class Config:
    SECRET_KEY = os.environ.get('LIBL_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('LIBL_SQLALCHEMY_DATABASE_URI')
