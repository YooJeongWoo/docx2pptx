from Docx2PptxConverter.source import wordtopclass, additionalmod


class ClassConverter:
    def word_to_pclass(self, TitleList):
        return wordtopclass.wordtopclass(TitleList)

    def add_additional_text(self, slide, text):
        additionalmod.add_additional_text(slide, text)

    def add_additional_image(self, slide, path):
        additionalmod.add_additional_image(slide, path)

    def modify_title(self, slide, text):
        additionalmod.modifytitle(slide, text)

    def modify_layout(self, slide, num):
        additionalmod.modifylayout(slide, num)