__author__ = 'ceremcem'

from aktos_dcs import *
from aktos_dcs_lib import Qt
Qt.initialize()

class MainWindow(Actor, Qt.QtGui.QMainWindow):
    def __init__(self):
        Qt.QtGui.QMainWindow.__init__(self)
        Actor.__init__(self)
        self.ui = Qt.loadUI('simulator.ui')
        self.ui.horizontalSlider.valueChanged.connect(self.emit_weight_msg)

    def emit_weight_msg(self, value):
        self.send({'WeightMessage': {'val': value}})

if __name__ == "__main__":
    import sys
    ProxyActor()
    app = Qt.QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.ui.show()
    Qt.greenlet_exec(app)