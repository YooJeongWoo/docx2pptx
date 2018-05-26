from GUI.StepBase import *


class Step3Window(StepBase):
    def __init__(self, parent=None):
        StepBase.__init__(self, parent)
        self.description = QTextBrowser()
        self.layout = QVBoxLayout()

        self.directory_browse_button = QPushButton("browse")
        self.directory_label = QLabel("set directory")
        self.save_directory = ""

        self.step = 3
        self.step_title.setText("Step 3")
        self.set_description()

        self.layout.addWidget(self.description)
        self.set_directory_browse_button()
        self.work_area.setLayout(self.layout)

        self.connect_signal_slot()

    def set_description(self):
        self.description.append("Select directory path to save presentation file")

    def set_directory_browse_button(self):
        button_widget = QWidget()
        button_widget_hlayout = QHBoxLayout()

        button_widget_hlayout.addWidget(self.directory_browse_button)
        button_widget_hlayout.addWidget(self.directory_label)
        button_widget_hlayout.addStretch()

        button_widget.setLayout(button_widget_hlayout)

        self.layout.addWidget(button_widget)

    def connect_signal_slot(self):
        self.directory_browse_button.clicked.connect(self.browse_single_directory)

    def browse_single_directory(self):
        self.save_directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.directory_label.setText(self.save_directory)
        self.parent.ppt_file_path = self.save_directory
        self.parent.enable_next_button()

