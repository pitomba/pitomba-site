import os
from functools import partial


get_path_to = partial(os.path.join, os.path.dirname(__file__))

DEBUG = False

TEMPLATE_PATH = get_path_to("templates")
STATIC_PATH = get_path_to("static")

LINKEDIN_API_KEY = "ldsc4e5x9426"
LINKEDIN_API_SECRET = "pwJnSz6ClZ6ktVyV"
LINKEDIN_USER_TOKEN = "b4776526-1d5b-4182-88e6-d7faa80b384f"
LINKEDIN_USER_SECRET = "f7b2ce2a-ab7f-4461-b8df-57c60ebc725b"

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
