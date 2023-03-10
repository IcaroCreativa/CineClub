import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *


class VKQLineEdit(QLineEdit):
    def __init__(self, parent=None, name=None, mainWindowObj=None):
        super(VKQLineEdit, self).__init__(parent)
        self.name = name
        self.setFixedHeight(40)
        self.mainWindowObj = mainWindowObj
        self.setFocusPolicy(Qt.ClickFocus)

    def focusInEvent(self, e):
        self.mainWindowObj.keyboardWidget.currentTextBox = self
        self.mainWindowObj.keyboardWidget.show()

        self.mainWindowObj.setStyleSheet("color:#ffffff ;border: 1px solid #62727b;")
        super(VKQLineEdit, self).focusInEvent(e)

    def mousePressEvent(self, e):
        # print(e)
        # self.setFocusPolicy(Qt.ClickFocus)
        super(VKQLineEdit, self).mousePressEvent(e)
        



class KeyboardWidget(QWidget):
    def __init__(self, parent=None):
        super(KeyboardWidget, self).__init__(parent)
        self.currentTextBox = None

        self.signalMapper = QSignalMapper(self)
        self.signalMapper.mapped[int].connect(self.buttonClicked)

        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setAutoFillBackground(True)
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont('Arial', 12))
        layout.addWidget(self.text_box, 0, 0, 1, 13)
        
        self.names = ['a', 'z', 'e','é', 'r', 't', 'y', 'u', 'i', 'o', 'p', '^', '$',
                 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'ù', '%', '@',
                 'w', 'x', 'c', 'v', 'b', 'n', ',', ';', ':', '!', '.', '(', ')',
                 ]

        self.num= ['/','*','-','+','7','8','9','0','4','5','6','+','1','2','3','.'
        ]
        positions = [(i + 1, j) for i in range(3) for j in range(13)]
        positionsnum = [(i + 1, j) for i in range(4) for j in range(4)]
        
        def build_keyboard(position,list_text):
            for position, name in zip(position,list_text):

                if name == '':
                    continue
                button = QPushButton(name)
                button.setFont(QFont('Roboto', 12))
                button.setFixedHeight(30)
                button.setFixedWidth(30)

                button.KEY_CHAR = ord(name)
                button.clicked.connect(self.signalMapper.map)
                self.signalMapper.setMapping(button, button.KEY_CHAR)
                layout.addWidget(button, *position)
        
        build_keyboard(positions,self.names)
        
        
        # Cancel button
        cancel_button = QPushButton('Cancel')
        cancel_button.setFixedHeight(25)
        cancel_button.setFont(QFont('Arial', 12))
        cancel_button.KEY_CHAR = Qt.Key_Cancel
        layout.addWidget(cancel_button, 5, 0, 1, 2)
        cancel_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(cancel_button, cancel_button.KEY_CHAR)
        cancel_button.setFixedWidth(60)

        # Cancel Clear
        clear_button = QPushButton('Clear')
        clear_button.setFixedHeight(25)
        clear_button.setFont(QFont('Arial', 12))
        clear_button.KEY_CHAR = Qt.Key_Clear
        layout.addWidget(clear_button, 5, 2, 1, 2)
        clear_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(clear_button, clear_button.KEY_CHAR)
        clear_button.setFixedWidth(60)

        # Space button
        space_button = QPushButton('Space')
        space_button.setFixedHeight(25)
        space_button.setFont(QFont('Arial', 12))
        space_button.KEY_CHAR = Qt.Key_Space
        layout.addWidget(space_button, 5, 4, 1, 3)
        space_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(space_button, space_button.KEY_CHAR)
        space_button.setFixedWidth(85)


        # Back button
        back_button = QPushButton('Back')
        back_button.setFixedHeight(25)
        back_button.setFont(QFont('Arial', 12))
        back_button.KEY_CHAR = Qt.Key_Backspace
        layout.addWidget(back_button, 5, 7, 1, 2)
        back_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(back_button, back_button.KEY_CHAR)
        back_button.setFixedWidth(60)



        # Enter button
        enter_button = QPushButton('Enter')
        enter_button.setFixedHeight(25)
        enter_button.setFont(QFont('Arial', 12))
        enter_button.KEY_CHAR = Qt.Key_Enter
        layout.addWidget(enter_button, 5, 9, 1, 2)
        enter_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(enter_button, enter_button.KEY_CHAR)
        enter_button.setFixedWidth(60)

        # Done button
        done_button = QPushButton('Done')
        done_button.setFixedHeight(25)
        done_button.setFont(QFont('Arial', 12))
        done_button.KEY_CHAR = Qt.Key_Home
        layout.addWidget(done_button, 5, 11, 1, 2)
        done_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(done_button, done_button.KEY_CHAR)
        done_button.setFixedWidth(60)

        self.setGeometry(0, 0, 480, 300)
        self.setLayout(layout)

    def buttonClicked(self, char_ord):

        txt = self.text_box.toPlainText()

        if char_ord == Qt.Key_Backspace:
            txt = txt[:-1]
        elif char_ord == Qt.Key_Enter:
            txt += chr(10)
        elif char_ord == Qt.Key_Home:
            self.currentTextBox.setText(txt)
            self.text_box.setText("")
            self.hide()
            return
        elif char_ord == Qt.Key_Clear:
            txt = ""
        elif char_ord == Qt.Key_Space:
            txt += ' '
        elif char_ord < 0x110000:
            txt += chr(char_ord)
        else:
            txt += ""

        self.text_box.setText(txt)


class KeyboardUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        first_name = VKQLineEdit(name='First Name', mainWindowObj=self)
        last_name = VKQLineEdit(name='Last Name', mainWindowObj=self)

        mainWidget = QWidget()
        layout = QGridLayout()
        layout.addWidget(first_name, 0, 0)
        layout.addWidget(last_name, 1, 0)

        self.keyboardWidget = KeyboardWidget()
        layout.addWidget(self.keyboardWidget, 0, 0, 10, 10)
        mainWidget.setLayout(layout)

        self.keyboardWidget.hide()

        self.setCentralWidget(mainWidget)

        self.statusBar().showMessage('Ready')

        self.setGeometry(0, 0, 480, 320)
        self.setWindowTitle('KeyBoard')
        self.show()


if __name__ == '__main__':
    from pathlib import Path
    path=Path().parent
    path=path/"QSS"/"ElegantDark.qss" # changer le nom du fichier .qss pour changer le styleSheet
    with open(path, "r") as f:
        _style = f.read()
    app = QApplication(sys.argv)
    app.setStyleSheet(_style)
    ex = KeyboardUI()
    ex.show()
    sys.exit(app.exec_())