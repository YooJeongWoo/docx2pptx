from GUI.StepBase import *
from PyQt5 import QtCore


class Step2Window(StepBase):
    def __init__(self, parent = None):
        StepBase.__init__(self, parent)

        self.step = 2
        self.step_title.setText("Step 2")

        self.v_layout = QVBoxLayout()
        self.detailed_work_area = QWidget()
        self.h_layout = QHBoxLayout()

        self.setting_group_box = QGroupBox()
        self.theme_widget = QWidget()
        self.theme_combo_box = QComboBox()
        self.main_title_widget = QWidget()
        self.main_title_line = QLineEdit()
        self.main_title_line.setPlaceholderText("set title of presentation")

        self.slide_layout_widget = QWidget()
        self.slide_layout_title = QLabel()
        self.slide_layout_combo_box = QComboBox()

        self.slide_image_widget = QWidget()
        self.slide_image_list_checkbox = QListView()
        self.slide_image_item_model = QStandardItemModel()

        self.slide_list_view = QListView()
        self.slide_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.detailed_setting_box = QGroupBox()

        self.model = QStandardItemModel(self.slide_list_view)

        self.set_slide_list_view()
        self.set_setting_view()
        self.set_detailed_setting_box()

        self.detailed_work_area.setLayout(self.h_layout)

        self.v_layout.addWidget(self.setting_group_box)
        self.v_layout.addWidget(self.detailed_work_area)

        self.work_area.setLayout(self.v_layout)

    def connect_signal_slot(self):
        self.slide_list_view.selectionModel().selectionChanged.connect(self.update_detailed_setting_view)
        self.main_title_line.textChanged.connect(self.update_next_button)
        self.slide_layout_combo_box.currentIndexChanged.connect(self.update_slide_layout)
        self.theme_combo_box.currentIndexChanged.connect(self.set_template_name)
        self.slide_image_item_model.itemChanged.connect(self.update_slide_image)

    def set_slide_list_view(self):
        self.slide_list_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.slide_list_view.setWindowTitle("Slide List")

        for slide in self.parent.p_class.slides:
            item = QStandardItem(slide.title_text)
            self.model.appendRow(item)

        self.slide_list_view.setModel(self.model)

        self.h_layout.addWidget(self.slide_list_view)

    def set_setting_view(self):
        self.setting_group_box.setTitle("Setting")

        hbl = QHBoxLayout()
        hbl.addWidget(self.theme_widget)
        hbl.addWidget(self.main_title_widget)
        hbl.addStretch()

        self.set_theme_widget()
        self.set_title_widget()

        self.setting_group_box.setLayout(hbl)

    def set_detailed_setting_box(self):
        self.detailed_setting_box.setTitle("Slide Setting")

        setting_v_layout = QVBoxLayout()

        slide_layout_hlayout = QHBoxLayout()
        slide_layout_hlayout.addWidget(self.slide_layout_title)
        slide_layout_hlayout.addWidget(self.slide_layout_combo_box)
        self.slide_layout_title.setText("Layout")
        layout_data = ["제목", "제목과 본문", "빈 슬라이드"]
        for layout in layout_data:
            self.slide_layout_combo_box.addItem(layout)

        self.slide_layout_widget.setLayout(slide_layout_hlayout)

        slide_image_hlayout = QHBoxLayout()
        slide_image_label = QLabel("Image")
        slide_image_hlayout.addWidget(slide_image_label)
        slide_image_hlayout.addWidget(self.slide_image_list_checkbox)
        self.slide_image_list_checkbox.setDisabled(True)
        self.slide_image_widget.setLayout(slide_image_hlayout)

        self.slide_image_item_model = QStandardItemModel()

        for image in self.parent.image_list:
            item = QStandardItem(image)
            item.setCheckable(True)
            self.slide_image_item_model.appendRow(item)

        self.slide_image_list_checkbox.setModel(self.slide_image_item_model)

        setting_v_layout.addWidget(self.slide_layout_widget)
        setting_v_layout.addWidget(self.slide_image_widget)
        setting_v_layout.addStretch()

        self.detailed_setting_box.setLayout(setting_v_layout)

        self.h_layout.addWidget(self.detailed_setting_box)

    def add_item(self, parent, elements):
        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.add_item(item, children)

    def set_theme_widget(self):
        hbl = QHBoxLayout()
        theme_label = QLabel("Theme")
        hbl.addWidget(theme_label)
        hbl.addWidget(self.theme_combo_box)
        self.theme_combo_box.addItem("Empty")
        self.theme_combo_box.addItem("Colorful")
        self.theme_combo_box.addItem("POSTECH")

        self.theme_widget.setLayout(hbl)

    def set_title_widget(self):
        hbl = QHBoxLayout()
        title_label = QLabel("Title")
        hbl.addWidget(title_label)
        hbl.addWidget(self.main_title_line)

        self.main_title_widget.setLayout(hbl)

    def update_detailed_setting_view(self):
        index = self.slide_list_view.currentIndex().row()
        self.slide_layout_combo_box.setCurrentIndex(self.parent.p_class.slides[index].layout_num)
        self.update_slide_image_widget()

    def update_slide_image_widget(self):
        self.slide_image_list_checkbox.setEnabled(True)
        for image in self.parent.image_list:
            if self.parent.p_class.slides[self.slide_list_view.currentIndex().row()].has_image(image):
                self.slide_image_item_model.item(self.parent.image_list.index(image)).setCheckState(
                    QtCore.Qt.Checked)
            else:
                self.slide_image_item_model.item(self.parent.image_list.index(image)).setCheckState(
                    QtCore.Qt.Unchecked)

    def update_next_button(self):
        if self.main_title_line.text() is "":
            self.parent.disable_next_button()
        else:
            self.parent.enable_next_button()
            self.parent.ppt_file_name = self.main_title_line.text()

    def update_slide_layout(self):
        self.parent.p_class.slides[self.slide_list_view.currentIndex().row()].layout_num = self.slide_layout_combo_box.currentIndex()

    def set_template_name(self):
        self.parent.p_class.set_template_name(self.get_template_name_with_index(self.theme_combo_box.currentIndex()))
        pass

    def update_slide_image(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.parent.p_class.slides[self.slide_list_view.currentIndex().row()].add_additional_image(str(item.text()))
        elif self.parent.p_class.slides[self.slide_list_view.currentIndex().row()].has_image(str(item.text())):
            self.parent.p_class.slides[self.slide_list_view.currentIndex().row()].remove_additional_image(str(item.text()))

    @staticmethod
    def get_template_name_with_index(index):
        return {
            0: None,
            1: "1.pptx",
            2: "POSTECH.pptx",
        }.get(index, None)

