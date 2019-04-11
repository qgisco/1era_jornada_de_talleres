from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QMessageBox)
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("custom_window.ui", self)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        QMessageBox.about(self, "Mensaje", "Hola Grupo de Usuarios QGIS Colombia")


app = QApplication([])
mainWindow = MainWindow()
mainWindow.show()
app.exec_()
