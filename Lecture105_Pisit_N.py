class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirCool(self):
        print("Turn On : Air")

class PickUp(Vehicle):
    pass

class Car(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass

pickUp1 = PickUp()
pickUp1.turnOnAirCool()

car1 = Car()
car1.turnOnAirCool()

van1 = Van()
van1.turnOnAirCool()

estatecar1 = EstateCar()
estatecar1.turnOnAirCool()