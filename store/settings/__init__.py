from .base import *

try:
    from .local import *
except ImportError:
    print('Can\'t fing module settings.local. Use settings.local.skeleton as a template to create it.')
