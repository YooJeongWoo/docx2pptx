from Docx2PptxConverter.source.slide import Slide
from Docx2PptxConverter.source.pclass import Pclass
from DocxParser.source.TitleClass import Title


#word to ppt class conversion, 파일이름, slidemaster_num, template_name 지정해주어야함
def wordtopclass(TitleList):
    prs = Pclass()

    '''
    #tree traversal
    traverse(prs, TitleList[0])
    prs.slides[0].layout_num = 0
    '''
    for i in range(len(TitleList)):
        temp_slide = Slide()
        temp_slide.set_title_text(TitleList[i].title)
        if len(TitleList[i].content) > 1:
            temp_list = TitleList[i].content
            temp_slide.add_additional_text(temp_list)

        prs.add_slide(temp_slide)

    return prs

'''
def traverse(prs, Title):
    temp_slide = Slide()
    temp_slide.set_title_text(Title.title)

    if len(Title.content) > 1: #본문에 강조된 부분이 있을경우
        temp_list = Title.content
        del temp_list[0]
        temp_slide.additional_text = temp_slide.additional_text + temp_list

    prs.add_slide(temp_slide)

    if len(Title.child) == 0:
        return
    for i in range(len(Title.child)):
        traverse(prs, Title.child[i])
'''