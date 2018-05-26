class Title:
    def __init__(self):
        self.index=0
        self.title=""
        self.parent=None
        self.child=[]
        self.content=[]

    def TreeConstructor(self,aparent):
        '''titlecontent is list , whose first element is title and if index==2 case, the others element
        are content. aparent is parent node, list is set of all node, titlecontent is list which contains
        title and content(if index==2)'''
        if(self.index==0):
            self.parent=None
        elif(self.index==1):
            self.parent=aparent
            aparent.child.append(self)
        else:
            self.parent=aparent
            aparent.child.append(self)





