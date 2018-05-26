from GUI.StepBase import *
from DocxParser import Parser
from Docx2PptxConverter import ClassConverter


class Step1Window(StepBase):
    def __init__(self, parent=None, filename=None):
        StepBase.__init__(self, parent)

        self.parser = Parser.ParserProgram()
        self.converter = ClassConverter.ClassConverter()

        self.description = QTextBrowser()
        self.layout = QVBoxLayout()
        self.file_browse_button = QPushButton("browse")
        self.file_label = QLabel("Select file(.docx)")
        self.file_label.setWordWrap(True)

        self.step = 1
        self.step_title.setText("Step 1")
        self.set_description()

        self.layout.addWidget(self.description)
        self.set_file_browse_button()
        self.work_area.setLayout(self.layout)

        self.connect_signal_slot()

    def set_description(self):
        self.description.append("Welcome to docx 2 pptx. \nBrowse your docx file to convert\n\n\n"
                                "Contributed by. OOP_TEAM1")

    def set_file_browse_button(self):
        button_widget = QWidget()
        button_widget_hlayout = QHBoxLayout()

        button_widget_hlayout.addWidget(self.file_browse_button)

        if self.parent.file_path is None:
            self.parent.disable_next_button()
        else:
            self.file_label.setText(self.parent.file_path)
            self.parent.enable_next_button()

        button_widget_hlayout.addWidget(self.file_label)
        button_widget_hlayout.addStretch()

        button_widget.setLayout(button_widget_hlayout)

        self.layout.addWidget(button_widget)

    def connect_signal_slot(self):
        self.file_browse_button.clicked.connect(self.browse_single_docx)

    def browse_single_docx(self):
        file_name = QFileDialog.getOpenFileName(self, 'Single File', "~/Desktop", '*.docx')

        self.parser.load_file(file_name[0])
        length = len(self.parser.titlelist)
        for d in range(length):
            print(self.parser.titlelist[d].title)
            if self.parser.titlelist[d].index == 2:
                print(self.parser.titlelist[d].content)

        self.parent.ppt_slide_list = self.converter.word_to_pclass(self.parser.titlelist).slides

        for slide in self.parent.ppt_slide_list:
            print(slide.title_text)

        self.file_label.setText(file_name[0])
        self.parent.file_path = file_name[0]
        self.parent.enable_next_button()

