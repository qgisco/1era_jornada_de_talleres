from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QMessageBox,
                             QGridLayout,
                             QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(400, 400)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        self.button = QPushButton(self, text="Mostrar mensaje")
        self.button.clicked.connect(self.show_message)
        gridLayout.addWidget(self.button, 0, 0)

    def show_message(self):
        QMessageBox.about(self, "Mensaje", "Hola Grupo de Usuarios QGIS Colombia")


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
