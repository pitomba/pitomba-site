from settings_base import *

PORT = 9082

SERVER_NAME = 'http://pitomba.org'

LOGGING['root']['handlers'] = ['file']
LOGGING['handlers']['file'] = {
    'level': 'INFO',
    'class': 'logging.FileHandler',
    'formatter': 'detailed',
    'filename': '/var/log/pitomba/app.log',
    'encoding': 'utf-8',
}
