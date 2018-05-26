from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class StepBase(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self)

        self.parent = parent

        self.step = 0
        self.ready_for_next_step = False

        self.step_title = QLabel("Step")
        self.work_area = QWidget()

        self.set_work_area()

        self.boxLayout = QVBoxLayout()
        self.boxLayout.addWidget(self.step_title)
        self.boxLayout.addWidget(self.work_area)
        self.boxLayout.addStretch()

        self.setLayout(self.boxLayout)

    def set_work_area(self):
        pass

    def update_step(self):
        self.step_title.update()
        self.work_area.update()

