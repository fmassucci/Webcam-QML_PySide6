from PySide6.QtGui import QImage
from PySide6.QtCore import Signal, Slot
from PySide6.QtQuick import QQuickImageProvider
from PySide6.QtCore import Qt

from camera.thread import CameraThread


class CamProvider(QQuickImageProvider):
    imageChanged = Signal(bool)
    cameraError = Signal(bool)
    image = None

    def __init__(self):
        super(CamProvider, self).__init__(QQuickImageProvider.Image)
        self.cam = CameraThread() 
        self.cam.updateFrame.connect(self.update_image)

    def requestImage(self, id, size, requestedSize):
        if id == "img?id=false" or "img?id=true":
            if self.image:
                img = self.image
            else:
                img = QImage(768, 640, QImage.Format_RGBA8888)
                img.fill(Qt.black)
        return img
        
    @Slot()
    def update_image(self, img):
        self.imageChanged.emit(True)
        self.image = img

    @Slot()
    def start(self):
        try:
            self.cam.start()
            print("Starting...")
        except:
            self.cameraError.emit(True)
          
    @Slot()
    def stop(self):
        self.cam.cap.release()
        self.cam.stop()      
        print("Finishing...")
    
    @Slot(float)
    def setLowerValue(self, value):
        self.cam.lower = int(value-1);

    @Slot(float)
    def setUpperValue(self, value):
        self.cam.upper = int(value-1);


  

