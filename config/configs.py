class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Brian8053@@127.0.0.1:5432/EMS'
    SECRET_KEY = 'some-random-key'

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = 'postgres://kgnjbgcdxvalcc:ad5883d755db80637caa2ae80c98d6d712aeaa80eaf2781b46eb01e8d09fe479@ec2-184-73-216-48.compute-1.amazonaws.com:5432/dfncka2a8m051s'
    SECRET_KEY = 'SOME-RANDOM-KEY'
