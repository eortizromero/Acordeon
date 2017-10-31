# -*-  coding: latin-1 -*-
from PyQt4.QtGui import QApplication
from .forms import Form
import sys


def create_app():
    app = QApplication(sys.argv)
    form = Form(450, 600,  'Application Name')
    form.create_form_gui('main_window')
    form.add_input_field('Nombre')
    form.show()
    try:
        with open('static/css/style.css', 'r') as t:
            tema = t.read()
        form.setStyleSheet(tema)
    except:
        print "css file not foud"
    form.setStyleSheet("#main_window{background: yellow;}")
    sys.exit(app.exec_())

