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

        self.bold_checkbox = QCheckBox()
        self.italic_checkbox = QCheckBox()
        self.highlight_checkbox = QCheckBox()
        self.underline_checkbox = QCheckBox()

        self.step = 1
        self.step_title.setText("Step 1")
        self.set_description()

        self.layout.addWidget(self.description)
        self.set_paragraph_option()
        self.set_file_browse_button()
        self.work_area.setLayout(self.layout)

        self.connect_signal_slot()

    def set_description(self):
        self.description.append("Welcome to docx 2 pptx. \n\n 1. Select default paragraph extract option."
                                "\n 2. Browse your .docx file to convert\n"
                                "\n\n"
                                "Contributed by. \nPOSTECH 2018-spring OOP_TEAM1\n"
                                "JW Yoo, DH Kang, JH Choi, JH Ha, JY Sim, HK Kim")

    def set_paragraph_option(self):
        gbx = QGroupBox()
        hbl = QHBoxLayout()

        gbx.setTitle("paragraph extract option")
        self.bold_checkbox.setText("Bold")
        self.italic_checkbox.setText("Italic")
        self.highlight_checkbox.setText("Highlight")
        self.underline_checkbox.setText("Underline")

        hbl.addWidget(self.bold_checkbox)
        hbl.addWidget(self.italic_checkbox)
        hbl.addWidget(self.highlight_checkbox)
        hbl.addWidget(self.underline_checkbox)

        self.enable_check_box()

        self.bold_checkbox.setChecked(self.parent.paragraph_option_list[0])
        self.italic_checkbox.setChecked(self.parent.paragraph_option_list[1])
        self.highlight_checkbox.setChecked(self.parent.paragraph_option_list[2])
        self.underline_checkbox.setChecked(self.parent.paragraph_option_list[3])

        gbx.setLayout(hbl)
        self.layout.addWidget(gbx)

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
        self.set_checked_button()
        boolist = self.parent.paragraph_option_list
        try:
            self.parser.set_parserobject(Bold=boolist[0], Italic=boolist[1], Highlight=boolist[2], UnderLine=boolist[3])
            self.parser.load_file(file_name[0])
            self.disable_check_box()
            # length = len(self.parser.titlelist)
            # for d in range(length):
            #     print(self.parser.titlelist[d].title)
            #     if self.parser.titlelist[d].index == 2:
            #         print(self.parser.titlelist[d].content)

            self.parent.p_class = self.converter.word_to_pclass(self.parser.titlelist)

            # for slide in self.parent.ppt_slide_list:
            #     print(slide.title_text)

            self.parent.image_list = self.parser.load_image(file_name[0])

            self.file_label.setText(file_name[0])
            self.parent.file_path = file_name[0]
            self.parent.enable_next_button()

        except:
            msg = QMessageBox()
            msg.setText("input .docx file format not supported")

    def set_checked_button(self):
        self.parent.paragraph_option_list[0] = self.bold_checkbox.isChecked()
        self.parent.paragraph_option_list[1] = self.italic_checkbox.isChecked()
        self.parent.paragraph_option_list[2] = self.highlight_checkbox.isChecked()
        self.parent.paragraph_option_list[3] = self.underline_checkbox.isChecked()

    def disable_check_box(self):
        self.bold_checkbox.setDisabled(True)
        self.italic_checkbox.setDisabled(True)
        self.highlight_checkbox.setDisabled(True)
        self.underline_checkbox.setDisabled(True)

    def enable_check_box(self):
        self.bold_checkbox.setEnabled(True)
        self.italic_checkbox.setEnabled(True)
        self.highlight_checkbox.setEnabled(True)
        self.underline_checkbox.setEnabled(True)
