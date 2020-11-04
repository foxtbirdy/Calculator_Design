import sys 

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt as Qtcore
from PyQt5.QtGui import *
from functools import partial


__version__ = "0.2"
__author__ = "Climax_[Code_Blender_7]"
__Tutorial__ = "Real Python"



class PyCalc(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Py Cal")
        self.setFixedSize(550,580)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        #GUI designing 
        self.mainLayout = QVBoxLayout()
        self._centralWidget.setLayout(self.mainLayout)
        self.IconUI()


        #Display control
        self._createDisplay()
        self.Buttons_config()
        



    def IconUI(self): 
        self.setWindowIcon(QIcon("icon.png"))


    def setDisplay_text(self , text):
        self.display.setText(text)
        self.display.setFocus()
        self.display.setFont(QFont("Arial" , 12))


    def displayText(self):
        return self.display.text()

    def clear_DisplayText(self):
        self.setDisplay_text("")


        #Display Config and design
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(55)
        self.display.setAlignment(Qtcore.AlignRight)
        self.display.setReadOnly(True)
        self.mainLayout.addWidget(self.display)
        self.setStyleSheet("background-color: \
                           hsl(216, 65.4%, 82%); \
                           color: hsl(45, 9.7%, 0%); \
                           border-style: solid; \
                           border-radius: 0.5px; border-width: 1px; \
                           border-color: hsl(177.7, 88%, 81%);")

    def Buttons_config(self):
        self.buttons = {}
        buttons_layout = QGridLayout()
        
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                  }    



        for btntext , pos in buttons.items():
            self.buttons[btntext] = QPushButton(btntext)
            self.buttons[btntext].setFixedSize(90,80)
            self.buttons[btntext].setFont(QFont("Montserrat" , 12))
            buttons_layout.addWidget(self.buttons[btntext] , pos[0] , pos[1]) 
        self.mainLayout.addLayout(buttons_layout)


class PyClacCRTL:

    def __init__(self, view, model):
        self._view = view
        self._evaluate = model
        self._connectSignals()



    def buildExpression(self, sub_exp):
        expression = self._view.displayText() + sub_exp
        self._view.setDisplay_text(expression)

        if self._view.displayText() == ERROR_MSG_user:
            self._view.clear_DisplayText()


    def calculateResult(self):
        Final_result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplay_text(Final_result)

    def _connectSignals(self):
        for btntext, btn in self._view.buttons.items():
            if btntext not in {"=" , "C"}:
                btn.clicked.connect(partial(self.buildExpression , btntext))

        self._view.buttons["C"].clicked.connect(self._view.clear_DisplayText)
        self._view.buttons['='].clicked.connect(self.calculateResult)
        self._view.display.returnPressed.connect(self.calculateResult)



ERROR_MSG_user = "Syntax ERROR"

def evaluateExpression(expression):

    try:
        result = str(eval(expression, {} , {}))
    except Exception:
        result = ERROR_MSG_user

    return result


def main():
    PyCal = QApplication(sys.argv)
    UI = PyCalc()
    UI.show()


    final_model = evaluateExpression

    PyClacCRTL(model = final_model , view=UI)
    sys.exit(PyCal.exec_())

if __name__ == "__main__":
    main()
    
    # Excuete Program
