from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow,QWidget,QMessageBox
import sys
from view import Ui_MainWindow # du fichier view.py import la class Ui_Mainwindow pour afficher l'interface graphique
from movie import get_movies,Movie
from subventana import Ui_Form




    

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Methode de la class Ui_MainWindow pour construire l'interface graphique
        self.populate_movies()
        self.setup_connections()
        self.subventana=Subventana()
        
        
    def setup_connections(self):
        
        #self.pushButton_add.clicked.connect(self.add_movie)
        self.lineEdit.returnPressed.connect(self.add_movie)
        text="Hola"
        self.pushButton_add.clicked.connect(lambda: self.add_movie(text)) # méthode pour passer une variable( ici text) à la fonction d'appel       self.pushButton_delete.clicked.connect(self.delete_movie)
        self.pushButton_new_screen.clicked.connect(self.mostrar_ventana)
        


    def mostrar_ventana(self):
        #self.subventana.setWindowOpacity(0.7) # permet de rendre transparente la subventana
        self.subventana.show()
        QMessageBox.information(self,"","POWER OFF")
        sys.exit()
    


    def populate_movies(self):

        for movie in get_movies():
            lw_item=QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole,movie)
            self.listWidget.addItem(lw_item)
    
    def add_movie(self,text):
        print(text)
        movie_title=self.lineEdit.text()
        movie_to_add=Movie(movie_title)
        if not movie_title:
            return False
        elif movie_to_add.add_movies():
            lw_item=QtWidgets.QListWidgetItem(movie_to_add.title)
            lw_item.setData(QtCore.Qt.UserRole,movie_to_add)
            self.listWidget.addItem(lw_item)
            self.lineEdit.setText("")


    def delete_movie(self):
        for selected_item in self.listWidget.selectedItems():
            movie=selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.listWidget.takeItem(self.listWidget.row(selected_item)) # permet de retirer le/s items de la liste

class Subventana(QWidget,Ui_Form,):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
            
        
        
    
    
           


def main():
    from pathlib import Path
    path=Path().parent
    path=path/"QSS"/"ManjaroMix.qss" # changer le nom du fichier .qss pour changer le styleSheet
    with open(path, "r") as f:
        _style = f.read()

    app = QApplication(sys.argv)
    app.setStyleSheet(_style)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
      
	
if __name__ == '__main__':
   main()