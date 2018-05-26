from PyQt5.QtWidgets import *
import GUI.GUI_Main as mainModule
import sys

# Run method for GUI docx2pptx program


def run():
    app = QApplication(sys.argv)

    screen = mainModule.MainWindow()
    screen.show()

    sys.exit(app.exec_())

