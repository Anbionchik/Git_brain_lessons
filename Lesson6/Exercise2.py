# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calculator(self, asphalt_mass_per_sqm, asphalt_thickness):
        asphalt_mass = self._length * self._width * asphalt_mass_per_sqm * asphalt_thickness
        return asphalt_mass


new_road = Road(5000, 20)
print(f'Для строительства дороги потребуется {new_road.asphalt_mass_calculator(asphalt_mass_per_sqm=25, asphalt_thickness=5)} кг асфальта.')

