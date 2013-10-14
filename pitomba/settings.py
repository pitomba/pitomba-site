from settings_base import *
from os.path import dirname, abspath, join


def get_local_file(path):
    import pdb;pdb.set_trace()
    return (lambda *x: abspath(join(dirname(path), *x)))


DEBUG = True
PORT = 9082

SERVER_NAME = 'http://0.0.0.0:%s' % PORT

UPLOAD_PATH = get_path_to('uploads')

