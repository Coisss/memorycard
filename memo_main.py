from main import *
from memo_card_layout import *
# from random import shuffle
# shuffle(radio_list)

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton

# def check_result ():
#     correct = answer.isChecked()
#     if correct:
#         lb_Result.setText(text_correct)
#         show_result()
#     else:
#         incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrond_answer3.isChecked()
#         if incorrect:
#             lb_Result.setText(Text_wrong)
#             show_result()

main_win = QWidget()

main_win.resize(600, 500)
main_win.setWindowTitle("Memory Card")
# the appearance of a window in a certain part of the screen
main_win.move(0, 0)

main_win.setLayout(layout_nav)

main_win.show()
app.exec()