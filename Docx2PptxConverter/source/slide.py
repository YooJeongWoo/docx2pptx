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
        self.additional_text = self.additional_text + text_list

    def add_additional_image(self, image):
        self.additional_image.append(image)

    def remove_additional_image(self, image):
        self.additional_image.remove(image)

    def has_image(self, image):
        if self.additional_image.count(image) is 0:
            return False
        else:
            return True

    '''
    def remove_additional_text(self, index):
        del self.additional_text[index]
        
    def remove_additional_image(self, index):
        del self.additional_image[index]
    '''