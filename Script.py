traffic_light='green'

speed_limit=60
class vehicle:
    def start_engine(self):
        message="Engine started"    
        print(message)

class car(vehicle):
    def __init__(self,make):
        self.make=make
    def start_engine(self):
        message="Car engine started"    
        print(message)

class bike(vehicle):
    def __init__(self,type):
        self.type=type
    def start_engine(self):
        message="bike engine started"    
        print(message)
        
obj=vehicle()
obj1=car("toyota")
obj2=bike("super bike")
obj.start_engine()
obj1.start_engine()
obj2.start_engine()
print(obj1.make)
print(obj2.type)
