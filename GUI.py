from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from  PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt
import sys
import keyboard
from RobotVision import UI_camera
from DrawTheVelocityGraph import GraphUI

class UI(QMainWindow):
    S = False
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('GUI.ui',self)
        self.show()

        self.start_stop.clicked.connect(self.start)
        self.up.clicked.connect(self.clickedUp)
        self.down.clicked.connect(self.clickedDown)
        self.left.clicked.connect(self.clickedLeft)
        self.right.clicked.connect(self.clickedRight) 
        self.open_camera_button.clicked.connect(self.openCamera)
        self.draw_graph_button.clicked.connect(self.openGraph)

    def clickedUp(self):
        self.leftvel.setText("Pushed UP Button")
    def clickedDown(self):
        self.leftvel.setText("Pushed DOWN Button")
    def clickedLeft(self):
        self.leftvel.setText("Pushed LEFT Button")
    def clickedRight(self):
        self.leftvel.setText("Pushed RIGHT Button")
    def openCamera(self):
        self.ui = UI_camera()
        self.ui.show()
    def openGraph(self):
        self.ui = GraphUI()
        self.ui.show()
    def start(self):
        UI.S = ~UI.S
        if (UI.S%2!=0):
            self.lineEdit.setText("Start")
            print(UI.S)
        else:
            self.lineEdit.setText("Stop")
            print(UI.S)

    def keyPressEvent(self, event):
        # print(event.text())
        if (event.text() == "w"):
            self.pressedUp()
        if (event.text() == "a"):   
            self.pressedRight()
        if (event.text() == "d"):
            self.pressedLeft()
        if (event.text() == "s"):
            self.pressedDown()
    
    def pressedUp(self):
        self.leftvel.setText("Press W")
    def pressedRight(self):
        self.leftvel.setText("Press R")
    def pressedLeft(self):
        self.leftvel.setText("Press L")
    def pressedDown(self):
        self.leftvel.setText("Press D")
def main():
    app = QApplication([])
    window = UI()
    app.exec_()

if __name__ == '__main__':
    main()