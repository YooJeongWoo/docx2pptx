from GUI.StepBase import *
from PPTMaker.PptxMaker import PptxMaker


class Step4Window(StepBase):
    def __init__(self, parent=None):
        StepBase.__init__(self, parent)

        self.maker = PptxMaker()

        self.description = QTextBrowser()
        self.layout = QVBoxLayout()

        self.step = 4
        self.step_title.setText("Step 4")
        self.set_description()

        self.layout.addWidget(self.description)
        self.work_area.setLayout(self.layout)

    def set_description(self):
        self.description.append("it's description of 4th step")

    def connect_signal_slot(self):
        self.parent.next_button.clicked.disconnect()
        self.parent.next_button.setText("Make")
        self.parent.prev_button.setDisabled(True)
        self.parent.next_button.clicked.connect(self.make_pptx_file)

    def make_pptx_file(self):
        self.maker.make_ppt(pclass=self.parent.p_class)
        msg = QMessageBox()
        msg.setText("pptx file is created!!")
        msg.exec_()



