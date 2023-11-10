class Auto:

    def __init__(self) -> None:
        pass

    def ride(self):
        print('Riding on a ground')

class Boat:
    def __init__(self) -> None:
        pass

    def swim(self):
        print('Floating on water')

class Amphibian(Auto, Boat):
    def __init__(self) -> None:
        pass
    
    def ride(self):
        super().ride()
    def swim(self):
        super().swim()

obj = Amphibian()
obj.ride()
obj.swim() 