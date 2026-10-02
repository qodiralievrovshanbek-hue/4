from abc import ABC, abstractmethod

class Vehicle(ABC):# shahriyor
    def __init__(self, marka, model, yil, tezlik):
        self._marka = marka
        self._model = model
        self._yil = yil
        self._tezlik = tezlik

    @property
    def speed(self):
        return self._tezlik

    @abstractmethod
    def start(self):
        print(f"{self._marka} {self._model} yurgizildi")

    @abstractmethod
    def move(self):
        print(f"{self._marka} {self._model} ketmoqda")

    def __str__(self):
        return f"{self._marka} {self._model} ({self._yil}), {self._tezlik} km/h"

    def __repr__(self):
        return f"{type(self).__name__}('{self._marka}', '{self._model}', {self._yil}, {self._tezlik})"

    def __bool__(self):
        return self._tezlik > 0

    def __eq__(self, other):
        return (self._marka, self._model, self._yil) == (other._marka, other._model, other._yil)

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self._tezlik > other._tezlik

    def __ge__(self, other):
        return self._tezlik >= other._tezlik

    def __lt__(self, other):
        return self._tezlik < other._tezlik

    def __le__(self, other):
        return self._tezlik <= other._tezlik

class Car(Vehicle):
    # shahriyor
    def start(self):
        print("Mashina yurdi")

    def move(self):
        print("Mashina ketmoqda")

class Motorcycle(Vehicle):
    def start(self):
        print("Mototsikl yurdi")

    def move(self):
        print("Mototsikl ketmoqda")

class Truck(Vehicle):
    def start(self):
        print("Yuk mashinasi yurdi")

    def move(self):
        print("Yuk mashinasi ketmoqda")

c1 = Car("Chevrolet", "Malibu", 2022, 180)
m1 = Motorcycle("Yamaha", "R1", 2021, 220)
t1 = Truck("Kamaz", "5320", 2019, 120)

vehicles = [c1, m1, t1]

for i in vehicles:
    print(i)
    i.start()
    i.move()

print(bool(c1))

print(c1 == m1)
print(c1 != t1)

print(c1 > m1)
print(t1 <= c1)