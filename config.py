import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    POSTS_PER_PAGE = 5
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    WEATHERAPIKEY = '&appid=c63608b30062c60e04f04ba158de1c84'
    UPLOADS_DEFAULT_DEST = 'app/static/img/'
    UPLOADS_DEFAULT_URL = 'https://0.0.0.0/app/static/img'
    UPLOADED_IMAGES_DEST = 'app/static/img/'
    UPLOADED_IMAGES_URL = 'https://0.0.0.0/app/static/img'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='libaixiu2014@gmail.com'
    MAIL_PASSWORD='cloud_app'
    MS_TRANSLATOR_KEY='5279b9fe290f4c84a7a4d15b926a4a45'
