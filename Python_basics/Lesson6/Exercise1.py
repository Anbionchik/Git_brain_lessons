# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    def __init__(self):
        self.__light_color = None
        self.__light_order = {'красный': 7, 'жёлтый': 2, 'зелёный': 10}

    def running(self):
        for color, wait_time in self.__light_order.items():
            self.set_color(color)
            self.get_color()
            time.sleep(wait_time)


    def set_color(self, color):
        self.__light_color = color

    def get_color(self):
        print(f"На светофоре горит {self.__light_color}.")


new_traffic_light = TrafficLight()
new_traffic_light.running()
new_traffic_light.get_color()
