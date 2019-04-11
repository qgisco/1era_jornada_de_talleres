from PyQt5 import (QtCore,
                   QtWidgets)
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QLabel,
                             QGridLayout,
                             QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(400, 400)
        self.setWindowTitle(".:: Hola mundo ::.")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        message = QLabel('Hola Grupo de Usuarios QGIS Colombia')
        message.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(message, 0, 0)


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()