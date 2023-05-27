from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
import numpy as np

class GraphUI(QMainWindow):
    def __init__(self):
        super(GraphUI, self).__init__()
        uic.loadUi('GraphUI.ui',self)
        self.show()
        self.setWindowTitle('The velocity of two wheel')
