from .base import *

DEBUG = True

SECRET_KEY = '-w!=11h@0itj#**+r$zhg(2g8_+bsz(nbq*ja*nt6@=xd%x_-y'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thirteen',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}