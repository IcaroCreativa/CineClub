import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.VirtualKeyboard 2.1
 
Rectangle {
    width: 200
    height: 200
    color: "green"
 
    
    TextField {
        width: parent.width
        placeholderText: "One line field"
        onAccepted: passwordField.focus = true
    }
    
    TextArea {
        id: textArea
        width: parent.width
        placeholderText: "Multiple line field"
        height: Math.max(206, implicitHeight)
    }
}