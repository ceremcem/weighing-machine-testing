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
        self.send({'IoMessage': {'pin_name': 'terazi-1', 'val': value}})
        self.send({'IoMessage': {'pin_name': 'vpin-2', 'val': value}})
        self.send({'IoMessage': {'pin_name': 'vpin-7', 'val': value}})
        self.send({'IoMessage': {'pin_name': 'vpin-8', 'val': value}})

    def handle_WeightMessage(self, msg):
        self.ui.horizontalSlider.valueChanged.disconnect(self.emit_weight_msg)
        self.ui.horizontalSlider.setValue(msg["val"])
        self.ui.horizontalSlider.valueChanged.connect(self.emit_weight_msg)


if __name__ == "__main__":
    import sys
    #ProxyActor(brokers="192.168.2.125:5012:5013 192.168.2.10:5012:5013")
    ProxyActor(brokers="192.168.2.157:5012:5013")
    app = Qt.QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.ui.show()
    Qt.greenlet_exec(app)
