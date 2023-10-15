from main import *
from memo_card_layout import *

from PyQt5.QtWidgets import QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

main_win = QWidget()

main_win.resize(600, 500)
main_win.setWindowTitle("Memory Card")
# the appearance of a window in a certain part of the screen
main_win.move(0, 0)

main_win.setLayout(layout_nav)

main_win.show()
app.exec()