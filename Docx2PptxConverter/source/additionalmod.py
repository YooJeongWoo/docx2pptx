def add_additional_text(slide, text):
    slide.additional_text.append(text)

def add_additional_image(slide, path):
    slide.additional_image.append(path)

def modifytitle(slide, text):
    slide.title_text = text

def modifylayout(slide, num):
    slide.layout_num = num

def modifytemplate(pclass, template_name):
    pclass.template_name = template_name