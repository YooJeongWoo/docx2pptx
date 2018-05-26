from GUI.StepBase import *
from PPTMaker.PptxMaker import PptxMaker


class Step4Window(StepBase):
    def __init__(self, parent=None):
        StepBase.__init__(self, parent)

        self.maker = PptxMaker()

        self.description = QTextBrowser()
        self.layout = QVBoxLayout()
        self.ppt_make_button = QPushButton("make")

        self.step = 4
        self.step_title.setText("Step 4")
        self.set_description()

        self.layout.addWidget(self.description)
        self.set_file_browse_button()
        self.work_area.setLayout(self.layout)

        self.connect_signal_slot()

    def set_description(self):
        self.description.append("it's description of 4th step")

    def set_file_browse_button(self):
        button_widget = QWidget()
        button_widget_hlayout = QHBoxLayout()

        button_widget_hlayout.addWidget(self.ppt_make_button)
        button_widget_hlayout.addStretch()

        button_widget.setLayout(button_widget_hlayout)

        self.layout.addWidget(button_widget)

    def connect_signal_slot(self):
        self.ppt_make_button.clicked.connect(self.make_pptx_file)

    def make_pptx_file(self):
        self.maker.make_ppt(pclass=self.parent.p_class,
                            filename=self.parent.ppt_file_path + "/" + self.parent.ppt_file_name)


