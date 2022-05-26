from Swiat import *
from Rosliny import *
from Zwierzeta import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QPushButton, QLabel
import sys

L = [Owca(1, 1), Owca(2, 2), Owca(1, 0), Wilk(0, 0), Antylopa(4, 4), BarszczSosnowskiego(5, 5), Zolw(3, 4), Trawa(6, 6), Lis(5, 7), CyberOwca(5, 6)]

#S = Swiat(10, 10, L)
#S.symuluj(15)
app = QApplication([])
label = QLabel("hello wolrd")
label.show()
app.exec_()

