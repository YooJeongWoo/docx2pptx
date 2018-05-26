import Parser
Program=Parser.ParserProgram()
Program.set_parserobject(True,False,False,False)
str="test.docx"
Program.load_file(str)
#아래는 사용 예시입니다.
length=len(Program.titlelist)
for d in range(length):
    print(Program.titlelist[d].title)
    if Program.titlelist[d].index==2:
        contentlen=len(Program.titlelist[d].content)
        print(Program.titlelist[d].content)
