# -*-  coding: latin-1 -*-
from PyQt4.QtGui import QApplication
from .forms import Form
import sys


def _get_static_file():
    root_static_path = 'static/'
    return root_static_path


def _get_default_name():
    return 'Application Name'


def _get_default_css():
    css = """
    #main_window{background: #FFF;}
    """
    return css


class App(object):
    def __init__(self, name=None):
        self.with_css = False
        if name is not None:
            self.name = name
            if self.name == '':
                self.name = _get_default_name()
            return
        self.name = _get_default_name()

    def application(self, type_app='form'):
        if type_app == 'form':
            pass
        print type_app

    def create_app(self, width, height, width_fix, with_css):
        app = QApplication(sys.argv)
        form = Form(width, height, self.name, width_fix)
        form.create_form_gui('main_window')
        form.add_input_field('Nombre')
        form.show()
        css_path = _get_static_file()
        def_css = _get_default_css()
        if with_css:
            try:
                with open('{}css/style.css'.format(css_path), 'r') as t:
                    tema = t.read()
                app.setStyleSheet(tema)
            except:
                print "css file not found, loading default css styles"
                app.setStyleSheet(def_css)
        else:
            app.setStyleSheet(def_css)
        app.setStyle('cleanlooks')
        sys.exit(app.exec_())

    def run(self,
            width=None,
            height=None,
            width_fixed=False,
            load_css=False,
            is_form=True):
        width_app, height_app, width_fixed_app = 400, 600, False
        if width is not None:
            width_app = width
        if height is not None:
            height_app = height
        if width_fixed is not False:
            width_fixed_app = width_fixed
        if load_css:
            self.with_css = load_css
        self.create_app(width_app, height_app, width_fixed_app, self.with_css)


