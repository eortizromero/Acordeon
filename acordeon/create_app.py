# -*-  coding: latin-1 -*-
import sys

from PyQt4.QtGui import QApplication
from components import Form


def _get_static_file():
    root_static_path = 'static/'
    return root_static_path


def _get_default_name():
    return 'Application Name'


def _get_default_css():
    css = """
    #main_window{background: #FFF;}
    QLineEdit{border:1px solid #AAA;padding:2px 5px; font-size:12px; border-radius:2px;}
    """
    return css


class App(object):
    def __init__(self, name=None, type=None):
        self.with_css = False
        self.type = type
        self.app = QApplication(sys.argv)
        self.width_form = 0
        self.height_form = 0
        self.width_fixed = False
        self.name = name
        if type is None:
            self.type = 'form'
        if name is None:
            if self.name == '':
                self.name = _get_default_name()
        self.form = Form(title=self.name)

    def login(self, field=None, password=None):
        if field is None:
            field = "Username"
        if password is None:
            password = "Password"
        self.form.create_form_gui('main_window')
        self.form.add_input_field(field, 50, 220, 300, 40)
        self.form.add_password_field(password, 50, 280, 300, 40)
        self.form.show()

    def create_app(self, app, width, height, width_fix, with_css, is_form):
        self.width_form = width
        self.height_form = height
        self.width_fixed = width_fix
        if is_form:
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
            sys.exit(app.exec_())

    def run(self,
            width=None,
            height=None,
            width_fixed=False,
            load_css=False):
        width_app, height_app, width_fixed_app = 400, 600, False
        if width is not None:
            width_app = width
        if height is not None:
            height_app = height
        if width_fixed is not False:
            width_fixed_app = width_fixed
        if load_css:
            self.with_css = load_css
        app = self.app
        if self.type == 'form':
            is_form = True
            self.create_app(app, width_app, height_app, width_fixed_app, load_css, is_form)
        else:
            is_form = False
            self.create_app(app, width_app, height_app, width_fixed_app, load_css, is_form)


