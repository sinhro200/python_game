from cmath import sqrt
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QSizePolicy, QPushButton, QCheckBox, \
    QColorDialog, QLayout


class MyVerticalLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

    def addModule(self, module: QLayout):
        self.addLayout(module)
        # self.setAlignment(module,Qt.AlignTop)


class MyModule(QHBoxLayout):
    def __init__(self, name, defValue=None):
        super().__init__()
        self.initBody(name, defValue)

    def initBody(self, name, defValue):
        self.name = name
        self.body = self.createBody(defValue)
        self.addWidget(self.body)

    def createBody(self, defValue):
        pass

    def getValue(self):
        pass

    def setValue(self, value):
        pass


class MyLabeledModule(MyModule):

    def initBody(self, name, defValue):
        self.name = name
        self.label = QLabel(name)
        self.body = self.createBody(defValue)
        self.addWidget(self.label)
        self.addWidget(self.body)
        self.setAlignment(self.label, Qt.AlignHCenter)


class EditTextModule(MyLabeledModule):
    def createBody(self, defValue):
        self.text = QTextEdit(defValue)
        self.text.setFixedHeight(30)
        self.text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return self.text

    def getValue(self):
        return self.text.toPlainText()

    def setValue(self, value):
        self.text.setText(value.__str__())


class ButtonModule(MyModule):
    def __init__(self, name: List, action: List, defValue=None):
        self.action = action
        super().__init__(name, defValue)

    def initBody(self, name, defValue):
        self.name = name
        self.buttons = []
        for i in range(self.name.__len__()):
            button = QPushButton(self.name[i])
            button.pressed.connect(self.action[i])
            self.addWidget(button)
            self.buttons.append(button)


class BooleanModule(MyLabeledModule):
    def createBody(self, defValue):
        self.checkBox = QCheckBox()
        return self.checkBox

    def getValue(self):
        return self.checkBox.isChecked()

    def setValue(self, value):
        self.checkBox.setChecked(value)


class ColorModule(MyLabeledModule):
    def initBody(self, name, defValue):
        self.name = name
        self.label = QLabel(name)
        self.addWidget(self.label)

        self.btn_col1 = QPushButton()
        self.btn_col2 = QPushButton()
        self.btn_col3 = QPushButton()
        self.btn_col4 = QPushButton()
        self.btn_col1.pressed.connect(self.getColor1)
        self.btn_col2.pressed.connect(self.getColor2)
        self.btn_col3.pressed.connect(self.getColor3)
        self.btn_col4.pressed.connect(self.getColor4)

        self.addWidget(self.btn_col1)
        self.addWidget(self.btn_col2)
        self.addWidget(self.btn_col3)
        self.addWidget(self.btn_col4)

    def getValue(self):
        return [self.color1, self.color2, self.color3, self.color4]

    def setValue(self, value):
        self.color1 = value[0]
        self.color2 = value[1]
        self.color3 = value[2]
        self.color4 = value[3]
        self.setColor(self.btn_col1, value[0])
        self.setColor(self.btn_col2, value[1])
        self.setColor(self.btn_col3, value[2])
        self.setColor(self.btn_col4, value[3])

    def setColor(self, btn, color):
        btn.setStyleSheet("QWidget {background-color: %s}" % color.name())

    def getColor1(self):
        self.color1 = QColorDialog.getColor()
        self.setColor(self.btn_col1, self.color1)

    def getColor2(self):
        self.color2 = QColorDialog.getColor()
        self.setColor(self.btn_col2, self.color2)

    def getColor3(self):
        self.color3 = QColorDialog.getColor()
        self.setColor(self.btn_col3, self.color3)

    def getColor4(self):
        self.color4 = QColorDialog.getColor()
        self.setColor(self.btn_col4, self.color4)


class WinPathsModule(MyModule):
    splitter = " "
    def initBody(self, name, defValue):
        self.editText_array = []
        self.body = None
        self.name = name
        self.editText_array.clear()
        body = QVBoxLayout()
        self.addLayout(body)
        body.addWidget(
            QLabel(self.name)
        )
        if defValue == None:
            return
        size = len(defValue)
        # self.tableLayout.deleteLater()
        self.tableLayout = QVBoxLayout()
        for i in range(size):
            lineLayout = QHBoxLayout()
            for j in range(size):
                label = QLabel((i * 4 + j).__str__())
                label.setFixedSize(20, 20)
                lineLayout.addWidget(label)
            self.tableLayout.addLayout(lineLayout)
        # self.body.addLayout(tableLayout)
        # self.editTextsLayout.deleteLater()
        self.editTextsLayout = QVBoxLayout()
        for win_path in defValue:
            text = win_path[0].__str__()
            for rect_num in win_path[1:]:
                text = text + WinPathsModule.splitter + rect_num.__str__()
            editText = QTextEdit(text)
            editText.setMaximumWidth(200)
            editText.setMaximumHeight(30)
            self.editText_array.append(editText)
            self.editTextsLayout.addWidget(editText)

        body.addLayout(self.tableLayout)
        body.addLayout(self.editTextsLayout)


    def getValue(self):
        resArr = []
        for editText in self.editText_array:
            str_vals = editText.toPlainText().__str__()
            resArr.append(str_vals.split(WinPathsModule.splitter))
        return resArr

    def setValue(self, value):
        i=0
        for win_path in value:
            text = win_path[0].__str__()
            for rect_num in win_path[1:]:
                text = text + WinPathsModule.splitter + rect_num.__str__()
            editText = self.editText_array[i]
            editText.setText(text)
            i=i+1

