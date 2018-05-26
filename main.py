#dummy trial

from DocxParser.source.TitleClass import Title
from Docx2PptxConverter.ClassConverter import ClassConverter
#from pclasstoppt import makeppt

title1 = Title()
title1.index = 0
title1.title = "title1"
title1.parent = None

title2 = Title()
title2.index = 1
title2.title = "title2"
title2.parent = title1

title3 = Title()
title3.index = 1
title3.title = "title3"
title3.parent = title1

title4 = Title()
title4.index = 2
title4.title = "title4"
title4.parent = title2

title5 = Title()
title5.index = 2
title5.title = "title5"
title5.parent = title3

title1.child = [title2, title3]
title2.child = [title4]
title3.child = [title5]

title1.content = ["aamd", "fewf", "zzz"]
title2.content = ["qqq", "aaa"]

TitleList = [title1, title2, title3, title4, title5]

pclass = ClassConverter.word_to_pclass(TitleList)
pclass.set_template_name("1.pptx")

print(pclass.slides[0].additional_text)

print(pclass.slides[0].title_text)
print(pclass.slides[1].title_text)
print(pclass.slides[2].title_text)
print(pclass.slides[3].title_text)
print(pclass.slides[4].title_text)


