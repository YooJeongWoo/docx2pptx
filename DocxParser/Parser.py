from DocxParser.source.TitleClass import Title
import docx
import zipfile


class ParserProgram:
    def __init__(self):
        self.titlelist = []  # titlelist, which contain title classes
        self.tempParent1 = None  # index==1인  클래스의 부모를 가리키는 포인터
        self.tempParent2 = None  # index==2인 클래스의 부모를 가리키는 포인터
        self.tempParent3 = None  # index=3인 클래스의 부모를 가리키는 포인터
        self.isBold = True
        self.isItalic = True
        self.isHighlight = True
        self.isUnderLine = True
        self.doc=None

    def set_parserobject(self,Bold,Italic,Highlight,UnderLine):
        self.isBold = Bold
        self.isItalic = Italic
        self.isHighlight = Highlight
        self.isUnderLine = UnderLine

    def indentcount(self,aparagraph):
        i = 0
        icount = aparagraph.paragraph_format.left_indent
        if icount is not None:
            i = icount / 127000
        return i

    def load_file(self, filename):
        if len(self.titlelist) is not 0:
            while len(self.titlelist) is not 0:
                del(self.titlelist[0])

        self.doc = docx.Document(filename)
        paranum = len(self.doc.paragraphs)  # Number of paragraphs in docx file
        for i in range(paranum):
            icount = self.indentcount(self.doc.paragraphs[i])
            if self.doc.paragraphs[i].text != '':
                if icount == 0:
                    atitle = Title()
                    atitle.index = 0
                    atitle.title = self.doc.paragraphs[i].text
                    atitle.content.append(self.doc.paragraphs[i].text)
                    atitle.TreeConstructor(None)
                    self.tempParent1 = atitle
                    self.titlelist.append(atitle)
                elif icount == 1:
                    atitle = Title()
                    atitle.index = 1
                    atitle.title = self.doc.paragraphs[i].text
                    atitle.content.append(self.doc.paragraphs[i].text)
                    atitle.TreeConstructor(self.tempParent1)
                    self.tempParent2 = atitle
                    self.titlelist.append(atitle)
                elif icount == 2:
                    atitle = Title()
                    atitle.index = 2
                    atitle.title = self.doc.paragraphs[i].text
                    atitle.content.append(self.doc.paragraphs[i].text)
                    atitle.TreeConstructor(self.tempParent2)
                    self.tempParent3 = atitle
                    self.titlelist.append(atitle)
                else:
                    runlen = self.doc.paragraphs[i].runs.__len__()
                    transition = -1
                    BoldRunSet = ""
                    HighlightRunSet = ""
                    UnderLineRunSet = ""
                    ItalicRunSet = ""
                    for j in range(runlen):
                        if self.doc.paragraphs[i].runs[j].bold == True and self.isBold:
                            if transition == 0 or transition == -1:
                                BoldRunSet = BoldRunSet + self.doc.paragraphs[i].runs[j].text
                            elif transition == 1:
                                if ItalicRunSet != "":
                                    self.tempParent3.content.append(ItalicRunSet)
                                ItalicRunSet = ""
                            elif transition == 2:
                                if HighlightRunSet != "":
                                    self.tempParent3.content.append(HighlightRunSet)
                                HighlightRunSet = ""
                            elif transition == 3:
                                if UnderLineRunSet != "":
                                    self.tempParent3.content.append(UnderLineRunSet)
                                UnderLineRunSet = ""
                            transition = 0
                        elif self.doc.paragraphs[i].runs[j].italic == True and self.isItalic:
                            if transition == 0:
                                if BoldRunSet != "":
                                    self.tempParent3.content.append(BoldRunSet)
                                BoldRunSet = ""
                            elif transition == 1 or transition == -1:
                                ItalicRunSet = ItalicRunSet + self.doc.paragraphs[i].runs[j].text
                            elif transition == 2:
                                if HighlightRunSet != "":
                                    self.tempParent3.content.append(HighlightRunSet)
                                HighlightRunSet = ""
                            elif transition == 3:
                                if UnderLineRunSet != "":
                                    self.tempParent3.content.append(UnderLineRunSet)
                                UnderLineRunSet = ""
                            transition = 1
                        elif self.doc.paragraphs[i].runs[j].font.highlight_color is not None and self.isHighlight:
                            if transition == 0:
                                if BoldRunSet != "":
                                    self.tempParent3.content.append(BoldRunSet)
                                BoldRunSet = ""
                            elif transition == 1:
                                if ItalicRunSet != "":
                                    self.tempParent3.content.append(ItalicRunSet)
                                ItalicRunSet = ""
                            elif transition == 2 or transition == -1:
                                HighlightRunSet = HighlightRunSet + self.doc.paragraphs[i].runs[j].text
                            elif transition == 3:
                                if UnderLineRunSet != "":
                                    self.tempParent3.content.append(UnderLineRunSet)
                                UnderLineRunSet = ""
                            transition = 2
                        elif self.doc.paragraphs[i].runs[j].underline == True and self.isUnderLine:
                            if transition == 0:
                                if BoldRunSet != "":
                                    self.tempParent3.content.append(BoldRunSet)
                                BoldRunSet = ""
                            elif transition == 1:
                                if ItalicRunSet != "":
                                    self.tempParent3.content.append(ItalicRunSet)
                                ItalicRunSet = ""
                            elif transition == 2:
                                if HighlightRunSet != "":
                                    self.tempParent3.content.append(HighlightRunSet)
                                HighlightRunSet = ""
                            elif transition == 3 or transition == -1:
                                UnderLineRunSet = UnderLineRunSet + self.doc.paragraphs[i].runs[j].text
                            transition = 3
                        else:
                            if BoldRunSet != "":
                                self.tempParent3.content.append(BoldRunSet)
                                BoldRunSet = ""
                            elif ItalicRunSet != "":
                                self.tempParent3.content.append(ItalicRunSet)
                                ItalicRunSet = ""
                            elif HighlightRunSet != "":
                                self.tempParent3.content.append(HighlightRunSet)
                                HighlightRunSet = ""
                            elif UnderLineRunSet != "":
                                self.tempParent3.content.append(UnderLineRunSet)
                                UnderLineRunSet = ""
                            transition = -1
                    if j == runlen - 1:
                        if BoldRunSet != "":
                            self.tempParent3.content.append(BoldRunSet)
                            BoldRunSet = ""
                        elif ItalicRunSet != "":
                            self.tempParent3.content.append(ItalicRunSet)
                            ItalicRunSet = ""
                        elif HighlightRunSet != "":
                            self.tempParent3.content.append(HighlightRunSet)
                            HighlightRunSet = ""
                        elif UnderLineRunSet != "":
                            self.tempParent3.content.append(UnderLineRunSet)
                            UnderLineRunSet = ""
                        transition = -1

    def load_image(self, filename):
        z = zipfile.ZipFile(filename)
        all_files = z.namelist()
        images = filter(lambda x: x.startswith('word/media/'), all_files)
        for image in images:
            print(image)
            image1 = z.open(image).read()
            f = open(image[11:], 'wb')
            f.write(image1)
            f.close()
        z.close()

