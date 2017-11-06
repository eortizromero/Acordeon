# -*- coding: latin-1 -*-

try:
    import PyQt4
    import components
    from .create_app import App
except ImportError:
    print "PyQt4 Framework is not found, try install it. \
    \n\n\nOn Linux (debian distribution). \n\
    Open your terminal anf type 'sudo apt-get install python-qt4' \n\n\nOn windows: \n\
    Depending on your Windows Platform (x86/x64), download a wheel file from \
    https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4 and install with pip. \n\
    Example: pip install PyQt4?4.11.4?cp27?cp27m?win_amd64.whl."
    exit()
