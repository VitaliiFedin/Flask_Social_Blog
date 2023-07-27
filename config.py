import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'My_key'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'venator270399dayz@gmail.com'
    MAIL_PASSWORD = 'uklolbunjrjpupnn'
    FLASK_MAIL_SUBJECT_PREFIX = '[FLASK]'
    FLASK_MAIL_SENDER = 'venator270399dayz@gmail.com>'
    FLASK_ADMIN = 'vetal270399@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_POSTS_PER_PAGE = 10
    FLASK_FOLLOWERS_PER_PAGE = 5
    FLASK_COMMENTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:fed123321@localhost/test1'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:fed123321@localhost/test1'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:fed123321@localhost/test1'


class ProductionConfigMysql(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://vetal270399:fed123321@vetal270399.mysql.pythonanywhere-services.com/vetal270399$default'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
