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


class NotAnOfficeEquipment(Exception):
    def __init__(self, error_text):
        self.error_text = error_text
    

class WareHouse:
    def __init__(self):
        self.__stock = {}
        
    @staticmethod
    def is_office_equipment(unit):
        if not isinstance(unit, OfficeEquipment):
            return False
        else:
            return True

    def check_presence(self, unit):
        if unit.type not in self.__stock:
            return False
        else:
            if unit not in self.__stock[unit.type]:
                return False
            else:
                return True

    def receive_unit(self, unit):
        try:
            if not isinstance(unit, OfficeEquipment):
                raise NotAnOfficeEquipment("Данный объект не является офисным оборудованием.")
        except NotAnOfficeEquipment as e:
            print(e)
            return
        
        if self.check_presence(unit):
            print("Такой объект уже числится на складе.")
            return

        if unit.type not in self.__stock:
            self.__stock[unit.type] = [unit]
            print(f"{unit} успешно зачислен на склад.")
        else:
            self.__stock[unit.type].append(unit)
            print(f"{unit} успешно зачислен на склад.")
            
    def move_unit(self, unit, destination):
        if not self.check_presence(unit):
            print("На складе такого объекта нет.")
            return
        self.__stock[unit.type].remove(unit)
        print("{} перемещён в отдел {}".format(unit, destination))
        
    def show_stock(self, units_type=None):
        if units_type is not None:
            if units_type in self.__stock:                
                for unit in self.__stock[units_type]:
                    print(unit)
            else:
                print("Оборудования такого типа на складе нет.")
        else:
            for unit_type, units_list in self.__stock.items():
                print(f'Тип оборудования {unit_type}:')
                for unit in units_list:
                    print(unit)


class OfficeEquipment:
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.type = "Printer"

    def __str__(self):
        return "Принтер {} {}".format(self.manufacturer, self.model)

    @staticmethod
    def print_obj(obj):
        print(f"{obj} успешно напечатан.")


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.type = "Scanner"

    def __str__(self):
        return "Сканнер {} {}".format(self.manufacturer, self.model)

    @staticmethod
    def scan(obj):
        print(f"{obj} успешно просканирован.")


class MFU(OfficeEquipment):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)
        self.type = "MFU"

    def __str__(self):
        return "МФУ {} {}".format(self.manufacturer, self.model)

    @staticmethod
    def print_obj(obj):
        print(f"{obj} успешно напечатан.")

    @staticmethod
    def scan(obj):
        print(f"{obj} успешно просканирован.")
    
    def copy(self, obj):
        self.scan(obj)
        self.print_obj(obj)


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
new_warehouse.receive_unit(printer1)
new_warehouse.receive_unit(printer3)
new_warehouse.receive_unit(scanner1)
new_warehouse.receive_unit(scanner2)
new_warehouse.receive_unit(scanner3)
new_warehouse.receive_unit(MFU3)
new_warehouse.receive_unit(MFU1)
new_warehouse.receive_unit(MFU2)
new_warehouse.receive_unit("sdfasdf")
new_warehouse.move_unit(printer2, "Офис на втором этаже")


