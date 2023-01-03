from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QWidget, QLabel,
    QLineEdit, QVBoxLayout)
import sys
import random
 
 
class Subventana(QWidget):
    def __init__(self, parent=None):                     # REVISAR AQUI
        super().__init__()
        self.parent = parent                             # REVISAR AQUI  
        self.resize(240, 120)
        self.setWindowTitle("Subventana")
 
        texto = QLineEdit()                              # REVISAR AQUI
        texto.textChanged.connect(self.texto_cambiado)   # REVISAR AQUI
 
        layout = QVBoxLayout()
        layout.addWidget(texto)
        self.setLayout(layout)
 
    def texto_cambiado(self, texto):                      # REVISAR AQUI
        self.parent.etiqueta.setText(texto)               # REVISAR AQUI
 
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
 
        self.subventana = Subventana(self)                 # REVISAR AQUI
 
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.subventana.show)
        layout.addWidget(boton_mostrar)
        boton_ocultar = QPushButton("Ocultar subventana")
        boton_ocultar.clicked.connect(self.subventana.hide)
        layout.addWidget(boton_ocultar)
 
        self.etiqueta = QLabel("TEXTO SUBVENTANA")         # REVISAR AQUI
        layout.addWidget(self.etiqueta)                    # REVISAR AQUI
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())