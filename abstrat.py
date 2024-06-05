from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def tyre(self):
        pass
    def start(self):
        print('start a vehicle')
class car(vehicle):
    def tyre(self):
        print('4') 
class bike(vehicle):
    def stop(self):
        print("tyre") 
swift=car()
swift.start()
swift.tyre()
ns=bike()
ns.stop()