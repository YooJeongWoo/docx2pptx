import PPTMaker.source.pclasstoppt as maker


class PptxMaker:
    def make_ppt(self, pclass, filename):
        maker.makeppt(pclass, filename=filename)
