from .base import *

try:
    from .local import *
except ImportError:
    print('Can\'t fing module settings.local')
