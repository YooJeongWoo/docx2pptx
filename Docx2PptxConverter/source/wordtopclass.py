from Docx2PptxConverter.source.slide import Slide
from Docx2PptxConverter.source.pclass import Pclass


#word to ppt class conversion
def wordtopclass(TitleList):
    prs = Pclass(1, len(TitleList), "1.pptx")

    #tree traversal
    traverse(prs, TitleList[0])
    prs.slides[0].layout_num = 0
    return prs

def traverse(prs, Title):
    temp_slide = Slide(1, Title.title)
    prs.slides.append(temp_slide)

    if len(Title.child) == 0:
        return
    for i in range(len(Title.child)):
        traverse(prs, Title.child[i])
