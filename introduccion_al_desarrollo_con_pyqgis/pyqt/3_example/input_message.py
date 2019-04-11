from PyQt5.QtWidgets import (QMainWindow,
                             QMessageBox,
                             QApplication)
from input_message_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # QtWidgets.QMainWindow.__init__(self)
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn_show_message.clicked.connect(self.show_message)

    def show_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Bienvenido al curso de PYQGIS")
        msg.setText("Este es un mensaje para usted: \n\n {}".format(
            self.text_edit_message.toPlainText()))
        msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
