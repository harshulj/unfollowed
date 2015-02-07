try:
    from .development import *
except ImportError as e:
    print "Import Error in development"
    print e
    from .production import *
