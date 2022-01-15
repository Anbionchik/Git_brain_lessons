# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if self.speed == 0:
            self.speed = speed
            print(f"Машина начала движение со скоростью {self.speed} км/ч.")
        else:
            self.speed = speed
            print(f"Скорость движения изменена. Текущая скорость {self.speed} км/ч.")

    def stop(self):
        if self.speed == 0:
            print("Машина стоит на месте.")
        else:
            self.speed = 0
            print("Машина остановилась.")

    def turn(self, direction):
        print(f"Машина повернула в направлении: {direction}.")

    def show_speed(self):
        print(f'Скорость автомобиля составляет {self.speed} км/ч.')


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        print(f'Скорость автомобиля составляет {self.speed} км/ч.')
        if self.speed > 60:
            print("Автомобиль превышает скорость.")


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        print(f'Скорость автомобиля составляет {self.speed} км/ч.')
        if self.speed > 40:
            print("Автомобиль превышает скорость.")

class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


some_town_car = TownCar("Красный", "Opel")
print(some_town_car.color)
some_town_car.go(180)
print(some_town_car.speed)
some_town_car.show_speed()
some_town_car.stop()
print(some_town_car.speed)
some_town_car.show_speed()
print(some_town_car.is_police)
some_town_car.turn("Центр")

print()

some_work_car = WorkCar("Жёлтый", "Caterpillar")
print(some_work_car.color)
some_work_car.go(50)
print(some_work_car.speed)
some_work_car.show_speed()
some_work_car.stop()
print(some_work_car.speed)
some_work_car.show_speed()
print(some_work_car.is_police)
some_work_car.turn("Стройка")

print()

some_police_car = PoliceCar("Белый", "Chevrolet")
print(some_police_car.color)
some_police_car.go(100)
print(some_police_car.speed)
some_police_car.show_speed()
some_police_car.stop()
print(some_police_car.speed)
some_police_car.show_speed()
print(some_police_car.is_police)
some_police_car.turn("Центр")

print()

some_sport_car = SportCar("Белый", "Chevrolet")
print(some_sport_car.color)
some_sport_car.go(300)
print(some_sport_car.speed)
some_sport_car.show_speed()
some_sport_car.stop()
print(some_sport_car.speed)
some_sport_car.show_speed()
print(some_sport_car.is_police)
some_sport_car.turn("Центр")