import QtQuick 2.15
import QtQuick.Window 
import QtMultimedia
import QtQuick.Controls 6.3
import QtQuick.Layouts 6.3
import QtQuick.Dialogs
import QtQuick.Controls.Material 2.15


ApplicationWindow {
    
    Material.theme: Material.Dark
    Material.accent: Material.LightBlue
    
    visible: true
    width: 600
    height: 500
    title: "WebCam - Integration Pyside6/QML"


    Image {
        id: feedImage
        width: parent.width
        height: parent.height - 50
        fillMode: Image.PreserveAspectFit
        cache: false
        source: "image://camProvider/img"
        property bool counter: false

        function reloadImage() {
            counter = !counter
            source = "image://camProvider/img?id=" + counter
        }

        Text {
            id:textError
            text: qsTr("Camera not connected")
            visible: false
            color: "white"
            font.pointSize: 16
            anchors {
                verticalCenter: feedImage.verticalCenter
                horizontalCenter: feedImage.horizontalCenter
            }
        }
    }


    RowLayout {
        anchors.top: feedImage.bottom
        anchors.horizontalCenter: feedImage.horizontalCenter

        Button {
            id: btnStartCamera
            text: "Start Camera"
            onClicked: {
                camProvider.start();
                bwSwitch.enabled = true;
            }
        }
        
        Button {
            id: btnStopCamera
            text: "Stop Camera"
            onClicked: {
                camProvider.stop()
                bwSwitch.enabled = false;
             }
        }

        Switch {
            id: bwSwitch
            text: qsTr("Black and White")
            font.pointSize: 9 
            enabled: false                                


            onClicked: {
                if (bwSwitch.position == 1.0) {
                    camProvider.bw(1)
                    } else {
                    camProvider.bw(0)
                    }
            }
        }
    }
   
    Connections{
        target: camProvider

        function onImageChanged(image) {
            feedImage.reloadImage()
        }

        function onCameraError() {
            textError.visible = true;
        }
            
    }

}
    