#main에서 from Docx2PptxConverter.ClassConverter import ClassConverter
#Pclass와 Slide 클래스는 wordtopclass에 포함되어있음
from Docx2PptxConverter.source import wordtopclass

class ClassConverter:
    def word_to_pclass(TitleList):
        return wordtopclass.wordtopclass(TitleList)

    #Pclass method: set_filename, set_slidemaster_num, set_slide_num, set_template_name, add_slide
    #Slide method: set_layout_num, set_title_text, add_additional_text, add_additional_image