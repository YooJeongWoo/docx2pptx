from Docx2PptxConverter.source.slide import Slide
from Docx2PptxConverter.source.pclass import Pclass


#word to ppt class conversion, 파일이름, slidemaster_num, template_name 지정해주어야함
def wordtopclass(TitleList):
    prs = Pclass()

    #tree traversal
    traverse(prs, TitleList[0])
    prs.slides[0].layout_num = 0
    return prs

def traverse(prs, Title):
    temp_slide = Slide()
    temp_slide.set_title_text(Title.title)

    prs.add_slide(temp_slide)

    if len(Title.child) == 0:
        return
    for i in range(len(Title.child)):
        traverse(prs, Title.child[i])
