# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером.")


new_pen = Pen("Bic")
new_pencil = Pencil("Bic")
new_handle = Handle("Bic")

new_pen.draw()
new_pencil.draw()
new_handle.draw()