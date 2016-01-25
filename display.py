# -*- coding: utf-8 -*-
__author__ = 'ceremcem'

from aktos_dcs import *
from aktos_dcs_lib import Qt
Qt.initialize()

class MainWindow(Actor, Qt.QtGui.QMainWindow):
    def __init__(self):
        Qt.QtGui.QMainWindow.__init__(self)
        Actor.__init__(self)
        self.ui = Qt.loadUI('display.ui')


    def handle_WeightMessage(self, msg):
        print "gui received message: ", msg['val']
        self.ui.weight.display(msg['val'])

if __name__ == "__main__":
    import sys
    ProxyActor(brokers="192.168.2.107:5012:5013")
    app = Qt.QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.ui.show()
    Qt.greenlet_exec(app)
