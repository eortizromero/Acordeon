# -*- coding: latin-1 -*-

from PyQt4.QtGui import QMainWindow, \
    QWidget, QApplication

"""
class parent for main form with center widget

"""

class Form(QMainWindow):
    def __init__(self, width, height, title):
        super(Form, self).__init__()
        self.width_container, self.height_container = width / 2, height
        self.setMinimumSize(width, height)
        self.setWindowTitle(title)
        # self.center_main_window()

    def center_main_window(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def create_form_gui(self,  id_name):
        self.form_container = QWidget(self)
        self.w = (self.width() - self.width_container) / 2
        self.h = (self.height() - self.height_container) / 2
        self.form_container.setGeometry(self.w, self.h, self.width_container, self.height_container)
        self.form_container.setObjectName(id_name)

    def center_widget_form(self):
        self.width_center_form = (self.width() - (self.width_container * 2)) / 2
        self.height_center_form = (self.height() - self.height_container) / 2
        self.form_container.setGeometry(self.width_center_form, self.height_center_form, self.width_container * 2, self.height_container)

    def resizeEvent(self, event):
        self.center_widget_form()

