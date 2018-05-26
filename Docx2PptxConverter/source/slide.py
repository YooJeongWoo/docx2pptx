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

    def add_additional_text(self, text_list):
        self.additional_text = self.additional_list + text_list

    def add_additional_image(self, image_path_list):
        self.additional_image = self.additional_image + image_path_list

    '''
    def remove_additional_text(self, index):
        del self.additional_text[index]
        
    def remove_additional_image(self, index):
        del self.additional_image[index]
    '''