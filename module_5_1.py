class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")  # Если этаж вне допустимого диапазона
        else:
            for floor in range(1, new_floor + 1):
                print(floor)  # Выводим этажи


# Создание объектов класса House
h1 = House('ЖК Эльбрус', 30)
h2 = House('Домик в деревне', 2)

# Вызов метода go_to для объектов
h1.go_to(5)
h2.go_to(10)