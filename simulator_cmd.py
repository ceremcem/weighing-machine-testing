__author__ = 'ceremcem'

from aktos_dcs import *

class WeightSimulator(Actor):
    def action(self):
        i = 0
        while True:
            print "sending weight message: ", i
            self.send({'WeightMessage': {'val': i}})
            i += 1
            sleep(0.5)

ProxyActor()
WeightSimulator()
wait_all()