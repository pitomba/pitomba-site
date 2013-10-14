from settings_base import *
from os.path import dirname, abspath, join

DEBUG = True
PORT = 9082

SERVER_NAME = 'http://0.0.0.0:%s' % PORT

UPLOAD_PATH = get_path_to('uploads')

