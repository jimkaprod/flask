# coding : utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  DBUSER = 'admin'
  DBPASS = 'admin'
  DBHOST = 'db'
  DBPORT = '5432'
  DBNAME = 'flaskdb'

  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
  #       'sqlite:///' + os.path.join(basedir, 'app.db')

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  print(SQLALCHEMY_DATABASE_URI)
