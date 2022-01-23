# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from random import randint


class WareHouse:
    def __init__(self):
        self.stock = {}
        self.id_list = []

    def check_presence(self, unit):
        if unit.type not in self.stock:
            return False
        else:
            if unit not in self.stock[unit.type]:
                return False
            else:
                return True

    def receive_unit(self, unit):
        # unit._id = self.create_id()
        # self.stock[unit._id] = unit
        # print("{} зачислен на склад под идентификатором {}.".format(unit, unit._id))
        if self.check_presence(unit):
            print("Такой объект уже числится на складе.")
            return

        if unit.type not in self.stock:
            self.stock[unit.type] = [unit]
            print(f"{unit} успешно зачислен на склад.")
        else:
            self.stock[unit.type].append(unit)
            print(f"{unit} успешно зачислен на склад.")

    def move_unit(self, unit, destination):
        if not self.check_presence(unit):
            print("На складе такого объекта нет.")
            return
        self.stock[unit.type].remove(unit)
        print("{} перемещён в отдел {}".format(unit, destination))

    # def create_id(self):
    #     while True:
    #         new_id = ''.join(["{}".format(randint(0, 9)) for _ in range(0, 6)])
    #         if not new_id in self.id_map:
    #             return new_id


class OfficeEquipment:
    def __init__(self, manufacturer, model):
        # self._id = None
        self.manufacturer = manufacturer
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.type = "Printer"

    def __str__(self):
        return "Принтер {} {}".format(self.manufacturer, self.model)


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.type = "Scanner"

    def __str__(self):
        return "Сканнер {} {}".format(self.manufacturer, self.model)


class MFU(OfficeEquipment):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.type = "MFU"

    def __str__(self):
        return "МФУ {} {}".format(self.manufacturer, self.model)


new_warehouse = WareHouse()
printer1 = Printer("Epson", "ABD-123")
printer2 = Printer("Canon", "QWERTY")
printer3 = Printer("Xerox", "3000")
scanner1 = Scanner("Epson", "978")
scanner2 = Scanner("Canon", "Super")
scanner3 = Scanner("Xerox", "2000")
MFU1 = MFU("Epson", "ABD-145")
MFU2 = MFU("Canon", "Foo")
MFU3 = MFU("Xerox", "3500")

new_warehouse.receive_unit(printer2)
new_warehouse.receive_unit(printer2)
new_warehouse.move_unit(printer2, "Офис на втором этаже")

