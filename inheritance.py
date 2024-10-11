class car:
    def __init__(self, type):
        self.type = type

    def start():
        print("car started...")

    def stop():
        print("car stoped")

class ToyotaCar(car):
    def __init__(self,name,color,type):
        self.name=name
        self.color=color
        super().__init__(type)

    @property
    def change_color(self,color):
        return color

car1=ToyotaCar("fortuner","diesel","black")
print(car1.name)
print(car1.type)
print(car.start())
car1.color="white"
print(car1.color)
