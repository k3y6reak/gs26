import os


basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
	SECRET_KEY = 'e?\xbaek\xfb\xda\x85\xb2\x94\x10\xf5\xec\xab[\xbcXZ\x06z\xad\xee?\x9f'
	DEBUG = True
	BCRYPT_LOG_ROUNDS = 13
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPDATE_FOLDER = 'update'
	UPLOAD_FOLDER = 'upload'