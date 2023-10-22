from main import *
from memo_main import *

from PyQt5.QtWidgets import QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox

def show_result ():
    pass

def show_question ():
    pass

layout_nav = QHBoxLayout()

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans4 = QVBoxLayout()

menu_btn = QPushButton("Меню")
calm_btn = QPushButton("Відпочити")
# RadioGroupBox = QGroupBox('Варіанти відповідей')
# RadioGroup = QButtonGroup()

# rbtn_1 = QRadioButton('')
# rbtn_2 = QRadioButton('')
# rbtn_3 = QRadioButton('')
# rbtn_4 = QRadioButton('' )
# RadioGroup.addButton(rbtn_1)
# RadioGroup.addButton(rbtn_2)
# RadioGroup.addButton(rbtn_3)
# RadioGroup.addButton(rbtn_4)

layout_nav.addWidget(menu_btn, alignment=Qt.AlignLeft)
layout_nav.addWidget(calm_btn, alignment=Qt.AlignRight)
# layout_ans1.addWidget(RadioGroup)

# answer = radio_list[0]
# wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]  