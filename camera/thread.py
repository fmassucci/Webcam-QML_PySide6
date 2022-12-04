import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Signal, QThread

class CameraThread(QThread):

    updateFrame = Signal(QImage)
    black_and_white = False
    
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        
    def run(self):
        self.cap = cv2.VideoCapture(0)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                pass
            if self.black_and_white == False:
                color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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