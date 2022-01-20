# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
# быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cloth_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def cloth_consumption(self):
        return 2*self.height + 0.3


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def cloth_consumption(self):
        return self.size/6.5 + 0.5


class ClothesManufacture:
    def __init__(self):
        self.order_list = []

    def add_position(self, element_type, size):
        if element_type.lower() == "suit":
            self.order_list.append(Suit(size))
        elif element_type.lower() == "coat":
            self.order_list.append(Coat(size))
        else:
            print('Данный тип одежды не изготавливается на производстве.')

    @property
    def cloth_consumption(self):
        result = 0
        for element in self.order_list:
            result += element.cloth_consumption()
        return result


new_factory = ClothesManufacture()
new_factory.add_position('Suit', 158)
new_factory.add_position('Suit', 156)
new_factory.add_position('Suit', 198)
new_factory.add_position('Suit', 145)
new_factory.add_position('Suit', 178)
new_factory.add_position('Suit', 179)
new_factory.add_position('coat', 46)
new_factory.add_position('coconut', 46)
new_factory.add_position('coat', 48)
new_factory.add_position('coat', 54)

print(new_factory.cloth_consumption)



