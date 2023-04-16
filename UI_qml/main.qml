import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 700
    height: 700
    title: "HelloApp"

Rectangle {
    color: "red"
    anchors.fill: parent

    Text {
        text: "WEEEEEEEEEE"
        font.pixelSize: 50
        color: "white"
        anchors.centerIn: parent
        RotationAnimator on rotation {
            running: true
            loops: Animation.Infinite
            from: 0
            to: 360
            duration: 1500
        }
    }
}
}

