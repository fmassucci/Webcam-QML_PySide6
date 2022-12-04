import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Signal, QThread
from camera.functions import colorSelection

class CameraThread(QThread):

    updateFrame = Signal(QImage)
    lower = 0
    upper = 179
    
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        
    def run(self):
        self.cap = cv2.VideoCapture(0)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                pass
            color_frame = colorSelection(frame, self.lower, self.upper)
            #color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            #color_frame = cv2.inRange(color_frame, (self.lower,0,0), (self.upper,255,255))

            qformat = QImage.Format_Indexed8
            if len(color_frame.shape) == 3:  
                if (color_frame.shape[2]) == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888                           
            img = QImage(color_frame, color_frame.shape[1], color_frame.shape[0],color_frame.strides[0], qformat)
            self.updateFrame.emit(img)
    
    def stop(self):
        self.ThreadActive = False
        self.quit()