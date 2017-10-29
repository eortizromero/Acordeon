#-*- coding: latin-1 -*-

try:
    from pyqtform import Form
    from PyQt4.QtGui import QApplication
except ImportError:
    print "Cannot initialize app, some libraries are requires"
    exit()

import sys


# TODO: Create decorator for init app and for each method app
def run_app():
    app = QApplication(sys.argv)
    title = 'App title'
    myform = Form(450, 600, title)
    myform.create_form_gui('main_window')
    myform.show()
    try:
        with open("static/css/style.css", "r") as theme:
            tema = theme.read()
        myform.setStyleSheet(tema)
    except:
        print "File Not Found"
    myform.setStyleSheet('#main_window{background: red;}')
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_app()
