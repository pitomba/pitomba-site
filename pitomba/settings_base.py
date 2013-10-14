import os
from functools import partial


get_path_to = partial(os.path.join, os.path.dirname(__file__))

DEBUG = True

TEMPLATE_PATH = get_path_to("templates")
STATIC_PATH = get_path_to("static")
STATIC_DEMO_PATH = STATIC_PATH + '/demo'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'NOTSET',
        'handlers': ['console'],
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
}

MEMCACHE = {
    'servers': ('localhost:11211',),
    'socket_timeout': 1,
}

EMAIL = {
    "server": "smtp.gmail.com",
    "port": 587,
}
