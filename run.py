## START RUNNING HERE ##

import os
import sys
from pathlib import Path
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
import camera.camera as cam

#Relative Path
scriptDir = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":

    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon(scriptDir + os.path.sep +"assets//video-camera.png"));
    engine = QQmlApplicationEngine()

    camProvider = cam.CamProvider()
    engine.rootContext().setContextProperty("camProvider", camProvider)
    engine.addImageProvider("camProvider", camProvider)

    qml_file = Path(__file__).resolve().parent / "qml/main.qml"
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())