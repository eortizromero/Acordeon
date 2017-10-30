#-*- coding: latin-1 -*-

try:
    from pyqtform import Form, create_app
except ImportError:
    print "Cannot initialize app, some libraries are requires"
    exit()

if __name__ == '__main__':
    create_app()
