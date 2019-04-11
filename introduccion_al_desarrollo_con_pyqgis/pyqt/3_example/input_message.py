from PyQt5.QtWidgets import (QMainWindow,
                             QMessageBox,
                             QApplication)
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("input_message_ui.ui", self)
        self.btn_show_message.clicked.connect(self.show_message)

    def show_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Bienvenido al curso de PYQGIS")
        msg.setText("Este es un mensaje para usted: \n\n {}".format(self.text_edit_message.toPlainText()))
        msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
