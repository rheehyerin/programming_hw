from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*'] #debug를 false로 할 경우 이 부분은 꼭 필수로 지정해주어야 한다.

DATABASES = {
    'default':{
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'ubuntu',
        'USER' : 'ubuntu',
        'PASSWORD' : 'withaskdjango!',
        'HOST' : '127.0.0.1',
    }
}
