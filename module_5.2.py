class House:                                                         #Создайте класс House
    def __init__(self, name, number_of_floors):                      #Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors присвойте им переданные значения.
        self.number_of_floors =  number_of_floors

    def __len__(self):                                                # должен возвращать кол-ва этажей self.number_of_floors
        return self.number_of_floors

    def __str__(self):                                                # должен возвращать строку с названием кол-ва этажей
        return (f'Название: {self.number_of_floors}, количество этажей: {self.number_of_floors}')


    def go_to(self, new_floor):                                     # Создайте метод go_to с параметром new_floor
        for i in range(1, new_floor + 1):                           # Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно)
            if 1 <= new_floor <= self.number_of_floors:             # Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку
                print(i)
            else:
                print('Такого этажа не существует')
                break

h1 = House('ЖК Горский', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)