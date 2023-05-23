from PyQt5.QtWidgets import *
from  PyQt5 import QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import sys

class UI_camera(QMainWindow):
    def __init__(self):
        super(UI_camera, self).__init__()
        uic.loadUi('RobotVision.ui',self)
        self.show()
        self.setWindowTitle('Robot Vison')

        self.pushButton.clicked.connect(self.cancelCamera)
        self.pushButton.clicked.connect(self.close)
        
        
        width = self.Image_label.width()
        height = self.Image_label.height()
        gray = QPixmap(width,height)
        gray.fill(QColor("darkGray"))
        self.Image_label.setPixmap(gray)

        self.Worker1 = Worker1()
        
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSLot)
        self.Worker1.start()
    def ImageUpdateSLot(self,img):
        self.Image_label.setPixmap(QPixmap.fromImage(img))
    def cancelCamera(self):
        self.Worker1.stop()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while True:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame ,cv2.COLOR_BGR2RGB)
                FlippedImg = cv2.flip(Image,1)
                ConvertToQtFormat = QImage(FlippedImg.data,FlippedImg.shape[1],FlippedImg.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640,480,Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()


def main():
    app = QApplication([])
    window = UI_camera()
    app.exec_()

if __name__ == '__main__':
    main()