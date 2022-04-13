class Airplane:
    def __init__(self, make, model, year, max_speed, odometer, is_flying):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying


    def airplane_motion(self, takeoff, fly, land):
        self.takeoff = takeoff
        self.fly = fly
        self.land = land


    def take_off(self):
        if self.is_flying == True:
            print(f'The Airplane {self.make}, {self.model}, made in {self.year}, is flying')


    def landing(self):
        if self.is_flying == False:
            print(f'The Airplane {self.make}, {self.model}, made in {self.year}, has landed')


    def fly(self, km):
        if self.is_flying == True:
            self.odometer  += km
            print(f'The Airplane {self.make} {self.model}, made in {self.year} is flying with max_speed {self.max_speed} and has overcome the distance {km} and in total {self.odometer}')

    def airplane_state(self):
        return (Airplane.take_off(self), Airplane.fly(self, 1000), Airplane.landing(self))


a = Airplane('Airbus', 'A320-214', 2020, 871, 11000, True)
a.take_off()
a.landing()
a.fly(1000)
a.airplane_state()