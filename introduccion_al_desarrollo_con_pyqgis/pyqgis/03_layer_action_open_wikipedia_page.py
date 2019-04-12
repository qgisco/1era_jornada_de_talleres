from qgis.PyQt.QtWidgets import QMessageBox

QMessageBox.information(None, "Feature id", "feature id de '[%name%]' is [% $id %]")

reply = QMessageBox.question(None, 
            "Pregunta",
            "¿Quieres abrir la pág de Wikipedia del aeropuerto '[%name%]'?",
            QMessageBox.Yes, QMessageBox.No)

if reply == QMessageBox.Yes:
    import webbrowser
    webbrowser.open("[%wikipedia%]")
