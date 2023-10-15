from main import *
from memo_main import *

from PyQt5.QtWidgets import QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

layout_nav = QHBoxLayout()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

menu_btn = QPushButton("Меню")

layout_nav.addWidget(menu_btn, alignment=Qt.AlignCenter)


