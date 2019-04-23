import os

from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

DialogBase, DialogType = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'zoom_to_state.ui'))

class PluginDialog(QDialog, DialogBase):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        

