
import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:omega@localhost/association_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "jimalsahra"