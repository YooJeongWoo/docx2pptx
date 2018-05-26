class Slide:
    def __init__(self):
        self.layout_num = 1
        self.title_text = None
        self.additional_text = []
        self.additional_image = []

    def set_layout_num(self, layout_num):
        self.layout_num = layout_num

    def set_title_text(self, title_text):
        self.title_text = title_text

    def add_additional_text(self, text):
        self.additional_text.append(text)

    def add_additional_image(self, image_path):
        self.additional_image.append(image_path)