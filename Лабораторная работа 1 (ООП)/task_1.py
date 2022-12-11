# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Car:
    def __init__(self, model: str, max_velocity: int, fuel: Union[int, float], fuel_consumption: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Car"
        :param model: Модель машины
        :param max_velocity: Максимальная скорость
        :param fuel: Запас бензина
        :param fuel_consumption: Расход бензина

        Примеры:
        >>> my_car = Car('Hyundai Solaris', 185, 30, 7.2) # Инициализация экземпляра класса
        """
        if not isinstance(model, str):
            raise TypeError('Модель должна быть в виде строки.')
        self.model = model

        if not isinstance(max_velocity, int):
            raise TypeError('Максимальная скорость должна выражаться целым числом.')
        if not max_velocity > 0:
            raise ValueError('Максимальная скорость должна быть положительным числом.')
        self.max_velocity = max_velocity

        if not isinstance(fuel, (int,float)):
            raise TypeError('Запас топлива должен выражаться числом.')
        if fuel < 0:
            raise ValueError('Запас топлива не может быть меньше 0')
        self.fuel = fuel

        if not isinstance(fuel_consumption, (int,float)):
            raise TypeError('Потребление топлива должено выражаться числом.')
        if fuel_consumption < 0:
            raise ValueError('Потребление топлива не может быть меньше 0')
        self.fuel_consumption = fuel_consumption

    def tank_up(self) -> int:
        """
        Функция заправляет машину
        :return: Количество топлива после заправки
        Примеры:
        >>> my_car = Car('Hyundai Solaris', 185, 0, 7.2)
        >>> my_car.tank_up()
        """
        ...

    def go_go_go(self, velocity: Union[int, float], time: Union[int, float]) -> Union[int, float]:
        """
        Машина едет по дороге

        :param self: Все параметры машины
        :param velocity: Текущая скорость
        :param time: Время езды
        :return: Пройденная дистанция
        Примеры:
        >>> my_car = Car('Hyundai Solaris', 185, 30, 7.2)
        >>> my_car.go_go_go(150, 10)
        """
        if not isinstance(velocity, (int,float)):
            raise TypeError('Скорость должна выражаться числом.')
        if velocity > self.max_velocity:
            raise ValueError('Скорость не может превышать максимальную!')
        ...

    def check_car(self, previous_check: Union[int,float]) -> bool:
        """
        Проверка необходимости прохождения ТО

        :param self: Сама машина
        :param previous_check: Время предыдущего ТО
        :return: Нужно ли проводить ТО
        Примеры:
        >>> my_car = Car('Hyundai Solaris', 185, 30, 7.2)
        >>> my_car.check_car(2)
        """
        ...


class Guitar:
    def __init__(self, guitar_type: str, strings: int, tuned: bool):
        """
        Создание и подготовка к работе объекта "Guitar"
        :param guitar_type: Разновидность гитары
        :param strings: Количество струн
        :param tuned: Настроена ли гитара
        Примеры:
        >>> my_guitar = Guitar('Fender Stratocaster', 6, True) # Инициализация экземпляра класса
        """
        if not isinstance(guitar_type, str):
            raise TypeError('Тип гитары представляется в виде строки.')
        self.guitar_type = guitar_type

        if not isinstance(strings, int):
            raise TypeError('Количество струн должно быть целым числом.')
        if strings < 0:
            raise ValueError('Количество струн не может быть отрицательным!')
        self.stings = strings

        if not isinstance(tuned, bool):
            raise TypeError('Тут нужен булевый тип')

    def play(self, composition: str) -> bool:
        """
        Играет какое-то музыкальное произведение
        :param composition: Название произведения
        :return: Сыграно или нет(нельзя сыграть на гитаре)
        Примеры:
        >>> my_guitar = Guitar('Fender Stratocaster', 6, True)
        >>> my_guitar.play('Smoke on the water')
        """
        ...

    def are_there_strings(self) -> bool:
        """
        Проверяет наличие струн на гитаре
        :return: Есть ли на гитаре струны
        Примеры:
        >>> my_guitar = Guitar('Fender Stratocaster', 0, False)
        >>> my_guitar.are_there_strings()
        """
        ...

    def tuning_guitar(self) -> bool:
        """
        Настраиваем гитару для игры
        :return: Возвращает настроенную гитару)))
        Примеры:
        >>> my_guitar = Guitar('Fender Stratocaster', 6, False)
        >>> my_guitar.tuning_guitar()
        """
        ...

class Student:
    def __init__(self, name: 'str', time: int, money: int, fullness: int):
        """
        Создание и подготовка к работе симуляции жизни объекта "Student"

        :param name: Имя студента
        :param time: Время, которое у него есть
        :param money: Деньги, которые у него есть
        :param fullness: Сытость
        Пример:
        >>> me = Student('Sofia', 5, 0, 5) # Инициализация экземпляра класса
        """

        if not isinstance(name,str):
            raise TypeError('Имя должно быть строкой.')
        self.name = name

        if not isinstance(time, int):
            raise TypeError('Доступное время должно быть целым числом.')
        if time < 0:
            raise ValueError('Времени, конечно, всегда нет, но оно не должно быть отрицательным')
        self.time = time

        if not isinstance(money, int):
            raise TypeError('Доступные деньги(плак-плак) должны быть целым числом.')
        if money < 0:
            raise ValueError('Денег, конечно, всегда нет, но их количество не должно быть отрицательным (даже если в кредиты залезть)')
        self.money = money

        if not isinstance(fullness, int):
            raise TypeError('Сытость должна выражаться целым числом.')
        if fullness < 0:
            raise ValueError('Отсутствие еды не означает, что её можно представлять отрицательным числом')
        self.fullness = fullness

    def is_alive(self) -> bool:
        """
        Проверяет жив ли человечек
        :param self: В основном стоит смотреть на сытость...
        :return: Возможна смерть от голода, другие возможные варианты в разработке
        Примеры:
        >>> me = Student('Sofia', 5, 1, 5)
        >>> me.is_alive()
        """
        ...

    def go_have_fun(self) -> Union[int,str]:
        """
        Пойти поразвлекаться при наличии времени
        :return: Да ничего не возвращает, просто трат драгоценное время
        Примеры:
        >>> me = Student('Sofia', 5, 0, 5)
        >>> me.go_have_fun()
        """
        if not self.time > 0:
            raise ValueError('У меня нет времени на всякую ерунду!')
        ...

    def eat(self, food: int) -> int:
        """
        Идем кушац
        :param food: Еда, которую можно скушать
        :return: Если что-то съесть, то сытость возрастет!
        Примеры:
        >>> me = Student('Sofia', 5, 0, 5)
        >>> me.eat(5)
        """
        if not isinstance(food, int):
            raise TypeError('Еда бывает разной, но тут её надо выразить числом')
        if not food > 0:
            raise ValueError('Лучше бы что-то нормальное предложили голодному студенту')
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
