from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()
window.setWindowTitle('Mi primer aplicación con PyQT')
QLabel('¡Hola mundo!', window)
window.show()
app.exec_()
