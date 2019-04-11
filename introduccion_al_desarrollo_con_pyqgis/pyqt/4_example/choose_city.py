from PyQt5.QtWidgets import (QMainWindow,
                             QMessageBox,
                             QApplication)
from PyQt5.uic import loadUi

DATA = {'AMAZONAS': ['LETICIA', 'EL ENCANTO', 'LA CHORRERA'],
        'ANTIOQUIA': ['MEDELLÍN', 'ABEJORRAL', 'ABRIAQUÍ', 'ALEJANDRÍA'],
        'ARAUCA': ['ARAUCA', 'ARAUQUITA', 'CRAVO NORTE', 'FORTUL'],
        'ATLÁNTICO': ['BARRANQUILLA', 'BARANOA', 'CAMPO DE LA CRUZ', 'CANDELARIA']}


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi("choose_city.ui", self)

        # load states
        for state in DATA:
            self.cb_state.addItem(state)

        self.cb_state.currentTextChanged.connect(self.on_combobox_state_changed)
        self.cb_state.currentTextChanged.emit(self.cb_state.currentText())

        self.button.clicked.connect(self.show_message)

    def on_combobox_state_changed(self, state):
        # Clear the previous selection
        self.cb_city.clear()

        # Load cities
        for city in DATA[state]:
            self.cb_city.addItem(city)

    def show_message(self):
        QMessageBox.about(self, "Mensaje",
                          "Seleccionaste: \n Departamento: {} \n Municipio: {}".format(self.cb_state.currentText(),
                                                                                       self.cb_city.currentText()))


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
