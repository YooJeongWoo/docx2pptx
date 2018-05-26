from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GUI.Step1 import *
from GUI.Step2 import *
from GUI.Step3 import *
from GUI.Step4 import *


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.step = 0
        self.file_path = None
        self.theme_index = 0
        self.p_class = None
        self.ppt_file_path = None
        self.ppt_file_name = ""

        self.layout = QVBoxLayout()
        self.step_window = QFrame()

        self.prev_button = QPushButton("prev", self)
        self.next_button = QPushButton("next", self)

        self.set_window_property()
        self.set_working_window()
        self.set_progress_button()

        self.connect_signal_slot()

        self.setLayout(self.layout)

    def set_window_property(self):
        label = QLabel("docx 2 pptx")
        font = QFont("Droid Sans", 20, QFont.Bold)
        label.setFont(font)
        self.layout.addWidget(label)
        self.setWindowTitle("docx2pptx")

    def set_working_window(self):
        self.step_window = Step1Window(parent=self)
        self.step = 1
        self.layout.addWidget(self.step_window)
        self.layout.addStretch()

    def set_progress_button(self):
        button_widget = QWidget()
        box_layout = QHBoxLayout()

        self.prev_button.setDisabled(True)
        self.next_button.setDisabled(True)

        box_layout.addStretch()
        box_layout.addWidget(self.prev_button)
        box_layout.addWidget(self.next_button)
        button_widget.setLayout(box_layout)

        self.layout.addWidget(button_widget)

    def connect_signal_slot(self):
        self.next_button.clicked.connect(self.next_step)
        self.prev_button.clicked.connect(self.prev_step)

    def next_step(self):
        self.layout.removeWidget(self.step_window)
        self.step_window.deleteLater()
        self.step += 1
        if self.step >= 4:
            self.step = 4
        self.step_window = self.get_step_window(self.step)
        self.layout.insertWidget(1, self.step_window)
        self.update_buttons()

    def prev_step(self):
        self.layout.removeWidget(self.step_window)
        self.step_window.deleteLater()
        self.step -= 1
        if self.step < 1:
            self.step = 1
        self.step_window = self.get_step_window(self.step)
        self.layout.insertWidget(1, self.step_window)
        self.update_buttons()

    def get_step_window(self, index):
        return {
            1: Step1Window(parent=self),
            2: Step2Window(parent=self),
            3: Step3Window(parent=self),
            4: Step4Window(parent=self),
        }.get(index, None)

    def update_buttons(self):
        if self.step is not 1:
            self.prev_button.setDisabled(False)

        if self.step is 1:
            self.prev_button.setDisabled(True)

        if self.step is 2:
            self.next_button.setDisabled(True)

        if self.step is 3:
            self.next_button.setDisabled(True)

    def disable_next_button(self):
        self.next_button.setDisabled(True)

    def enable_next_button(self):
        self.next_button.setEnabled(True)

