class Pclass:
    def __init__(self):
        self.filename = None
        self.slidemaster_num = None #레이아웃 set이 들어있는 slidemaster의 index
        self.slide_num = 0 #Slide 수
        self.template_name = None
        self.slides = []

    def set_filename(self, filename):
        self.filename = filename

    def set_slidemaster_num(self, slidemaster_num):
        self.slidemaster_num = slidemaster_num

    def set_template_name(self, template_name):
        self.template_name = template_name

    def add_slide(self, slide):
        self.slides.append(slide)
        self.slide_num += 1


