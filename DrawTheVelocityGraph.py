from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import numpy as np

class GraphUI(QApplication):
    def __init__(self):
        super(GraphUI, self).__init__()
        self.loadUI()
