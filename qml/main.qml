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
        spacing: 15

        Button {
            id: btnStartCamera
            text: "Start Camera"
            onClicked: {
                camProvider.start();
                rangeSlider.enabled = true;
            }
        }
        
        Button {
            id: btnStopCamera
            text: "Stop Camera"
            onClicked: {
                camProvider.stop()
                rangeSlider.enabled = false;
             }
        }
        RowLayout{

            spacing:5

            Text {
                id: slider1
                color: "white"
                text: qsTr("0")
            }

            RangeSlider {
                id:rangeSlider
                from: 1
                to: 180
                first.value: 1
                second.value: 180
                enabled: false
                stepSize : 1

                first.onMoved: {
                    camProvider.setLowerValue(rangeSlider.first.value)
                    slider1.text = qsTr(rangeSlider.first.value.toFixed(0).toString())
                }
                second.onMoved: {
                    camProvider.setUpperValue(rangeSlider.second.value)
                    slider2.text = qsTr(rangeSlider.second.value.toFixed(0).toString())
                }

            }

            Text {
                id: slider2
                color: "white"
                text: qsTr("180")
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
    