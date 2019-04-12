import qgis 
from qgis.PyQt.QtWidgets import QDockWidget
pythonConsole = qgis.utils.iface.mainWindow().findChild(QDockWidget, 'PythonConsole')
if not pythonConsole or not pythonConsole.isVisible():
    qgis.utils.iface.actionShowPythonDialog().trigger()
