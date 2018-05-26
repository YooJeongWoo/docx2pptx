from GUI.StepBase import *


class Step3Window(StepBase):
    def __init__(self, parent=None):
        StepBase.__init__(self, parent)
        self.description = QTextBrowser()
        self.layout = QVBoxLayout()
        self.file_browse_button = QPushButton("browse")

        self.step = 3
        self.step_title.setText("Step 3")
        self.set_description()

        self.layout.addWidget(self.description)
        self.set_file_browse_button()
        self.work_area.setLayout(self.layout)

        self.connect_signal_slot()

    def set_description(self):
        self.description.append("it's description of 3rd step")

    def set_file_browse_button(self):
        button_widget = QWidget()
        button_widget_hlayout = QHBoxLayout()

        button_widget_hlayout.addWidget(self.file_browse_button)
        button_widget_hlayout.addStretch()

        button_widget.setLayout(button_widget_hlayout)

        self.layout.addWidget(button_widget)

    def connect_signal_slot(self):
        self.file_browse_button.clicked.connect(self.browse_single_docx)

    def browse_single_docx(self):
        filePaths = QFileDialog.getOpenFileName(self, 'Single File', "~/Desktop", '*.docx')

