import math
import doctest

class AstronomicalObject():
    '''
    Базовый класс небесного тела.
    '''
    TO_SOLAR_MASS_UNITS = 1.989 * 10 ** 30 # [кг] Масса Солнца
    H = 70.8 # [км/(c*Мпк)] Постоянная Хаббла
    c = 3 * 10 ** 5 # [км/с] Скорость света
    def __init__(self, name: str, age: float, mass: float = None, mass_au: float = None, redshift: float = None):
        '''
        Создание и подготовка к работе объекта AstronomicalObject
        :param name: Название небесного тела
        :param age: Возраст небесного тела
        :param mass: Масса небесного тела
        :param mass_au: Масса небесного тела в относительных единицах массы Солнца
        :param redshift: Красное смещение (если наблюдается)

        Примеры:
        >>> planet = AstronomicalObject('Earth', 4.543*10**9, 5.9742*10**24)
        >>> planet1 = AstronomicalObject('X', 4.543*10**9)
        Traceback (most recent call last):
        ...
        TypeError: Input mass in kg or a.u.
        '''
        self.name = name
        self.age = age
        self.mass = mass
        self.redshift = redshift
        self._mass_au = mass_au
        if self.mass is None and self._mass_au is None:
            raise TypeError('Input mass in kg or a.u.')
        if self._mass_au is None:
            self._mass_au = self.mass_to_au()

    @property
    def mass_au(self):
        '''
        Делает приватный атрибут _mass_au свойством. Это необходимо потому, что масса в относительных
        единицах напрямую завязана на обычной массе и менять относительную массу без изменения обычной
        нельзя.
        :return: возвращает значение свойства mass_au

        Примеры:
        >>> planet = AstronomicalObject('Earth', 4.543*10**9, 5.9742*10**24)
        >>> print(planet.mass_au)
        3.0036199095022618e-06
        >>> planet.mass_au = 1
        Traceback (most recent call last):
        ...
        AttributeError: can't set attribute
        '''
        return self._mass_au

    def __str__(self):
        '''
        Строковый метод класса AstronomicalObject
        :return: Возвращает строку с наззванием и возрастом небесного тела

        Примеры:
        >>> planet = AstronomicalObject('Earth', 4.543*10**9, 5.9742*10**24)
        >>> print(planet)
        Небесное тело Earth массой 3e-06 солнечных масс и возрастом 4.54e+09 лет.
        '''
        return f'Небесное тело {self.name} массой {self._mass_au:.3} солнечных масс и ' \
               f'возрастом {self.age:.3} лет.'

    def __repr__(self):
        '''
        Возвращает валидную питоновскую строку
        :return: Возвращает валидную питоновскую строку

        Примеры:
        >>> planet = AstronomicalObject('Earth', 4.543*10**9, 5.9742*10**24)
        >>> print(repr(planet))
        AstronomicalObject(name='Earth', age=4.543e+09, mass=5.9742e+24, mass_au=3e-06, redshift=None)
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age:.4}, mass={self.mass:.5}, " \
               f"mass_au={self._mass_au:.3}, redshift={self.redshift})"

    def mass_to_au(self) -> float:
        '''
        Переводит массу из киллограмм в относительные единицы массы Солнца
        :return: Относительная масса объекта в единицах массы Солнца

        Примеры:
        >>> planet = AstronomicalObject('Earth', 4.543*10**9, 5.9742*10**24)
        >>> print(planet.mass_to_au())
        3.0036199095022618e-06
        '''
        return self.mass / self.TO_SOLAR_MASS_UNITS

    def how_far(self) -> float:
        '''
        Определяет расстояние от Земли до небесного тела используя закон Хаббла

        На самом деле зависимость намного сложнее, чем описано в данном методе. Корректные значения
        будут получаться только для z<<1 и то не всегда, потому что нужно учитывать различные эффекты,
        связанные с окружением галлактики. Например, для галактики Андромеда данная формула дает
        4.237 Мпк, тогда как реальное рассояние будет 0.765 Мпк.
        Для больших значений z при расчете расстояния используются различные модели, напримар
        lambda CDM model. Все эти модели слишком объемные для того, чтобы их расписывать в этом задании.

        :return: Расстояние от земли до небесного тела в Мега парсеках

        Примеры:
        >>> andromeda = AstronomicalObject('Andromeda Galaxy', 1.001*10**10, mass_au=1.23*10**12, redshift=0.001004)
        >>> print(andromeda.how_far())
        4.254237288135593
        '''
        if self.redshift is not None:
            return self.redshift * self.c / self.H


class SimpleBody(AstronomicalObject):
    '''
    Класс уединенного небесного тела
    '''
    SB_CONSTANT = 5.670367 * 10 ** (-8) # [Вт/(м^2*K^4)] Постоянная Стефана-Больцмана
    def __init__(self, name: str, age: float, mass: float, radius: float, temp: float,
                 mass_au: float = None, redshift: float = None):
        '''
        Создание и подготовка к работе объекта SimpleBody
        :param name: Название небесного тела
        :param age: Возраст небесного тела
        :param mass: Масса небесного тела
        :param radius: Радиус небесного тела
        :param temp: Средняя температура поверхности небесного тела
        :param mass_au: Масса небесного тела в относительных единицах массы Солнца
        :param redshift: Красное смещение (если наблюдается)

        Примеры:
        >>> planet = SimpleBody('Earth', 4.543*10**9, 5.9742*10**24, 637100, 288)
        '''
        super().__init__(name, age, mass, mass_au, redshift)
        self.radius = radius
        self.temp = temp

    def __repr__(self):
        '''
        Возвращает валидную питоновскую строку
        :return: Возвращает валидную питоновскую строку

        Примеры:
        >>> planet = SimpleBody('Earth', 4.543*10**9, 5.9742*10**24, 637100, 288)
        >>> print(repr(planet))
        SimpleBody(name='Earth', age=4.543e+09, mass=5.9742e+24, radius=637100, temp=288, mass_au=3e-06, redshift=None)
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age:.4}, mass={self.mass:.5}, " \
               f"radius={self.radius}, temp={self.temp}, mass_au={self._mass_au:.3}, redshift={self.redshift})"

    def energy_emitted(self):
        '''
        Данный метод позволяет определить  энергию, которую излучает тело со своей поверхности в еденицу времени.
        Испльзуется концепция абсолютно черного тела и закон Стефана-Больцмана.
        :return: Энергия излучаемая с поверхности объекта в Вт

        Примеры:
        >>> planet = SimpleBody('Earth', 4.543*10**9, 5.9742*10**24, 637100, 288)
        >>> print(planet.energy_emitted())
        1989785187909187.0
        '''
        return 4*math.pi*self.radius**2*self.SB_CONSTANT*self.temp**4


class Star(SimpleBody):
    '''
    Класс Звезды
    '''
    TO_SOLAR_RADIUS_UNITS = 6.957 * 10 ** (8) # [м^2] Радиус солнца
    SUN_LUMINOSITY = 3.827 * 10 ** 26 # [Вт] Светимость Солнца
    def __init__(self, name: str, age: float, mass: float, radius: float,
                 redshift: float, temp: float, mass_au: float=None, radius_su: float=None):
        '''
        Создание и подготовка к работе объекта Star
        :param name: Название звезды
        :param age: Возраст звезды
        :param mass: Масса звезды
        :param radius: Радиус звезды
        :param redshift: Красное смещение звезды
        :param temp: Температура Звезды
        :param mass_au: Масса звезды в относительных единицах массы Солнца
        :param radius_su: Радиус звезды в относительных единицах радиуса Солнца

        Примеры:
        >>> Sun = Star('Sun', 4.603*10**9, 1.989 * 10 ** (30), 6.9634*10**8, 0, 5778)
        '''
        super().__init__(name, age, mass, radius, temp, mass_au, redshift)
        self.radius_SU = radius_su
        if radius_su is None:
            self.radius_SU = radius_su

        self._luminosity = self.luminosity()

    def __repr__(self):
        '''
        Возвращает валидную питоновскую строку
        :return: Возвращает валидную питоновскую строку

        Примеры:
        >>> Sun = Star('Sun', 4.603*10**9, 1.989 * 10 ** (30), 6.9634*10**8, 0, 5778)
        >>> print(repr(Sun))
        Star(name='Sun', age=4.603e+09, mass=1.989e+30, radius=696340000.0, redshift=0, temp=5778, mass_au=1.0, radius_su=None)
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age:.4}, mass={self.mass:.5}, " \
               f"radius={self.radius}, redshift={self.redshift}, temp={self.temp}, mass_au={self._mass_au:.3}, " \
               f"radius_su={self.radius_SU})"

    def radius_in_su(self) -> float:
        '''
        Метод переводит радиус звезды в относительные единицы радиуса Солнца. Результат нужен для
        исмользования в методе evolution
        :return: Радиус звезды в относительные единицы радиуса Солнца

        Примеры:
        >>> Sun = Star('Sun', 4.603*10**9, 1.989 * 10 ** (30), 6.9634*10**8, 0, 5778)
        >>> print(Sun.radius_in_su())
        1.0009199367543482
        '''
        return self.radius / self.TO_SOLAR_RADIUS_UNITS

    def luminosity(self):
        '''
        Метод, который возвращает светимость звезды в относительных единицах светимости Солнца. Результат
        нужен для исмользования в методе evolution

        :return: Светимость звезды в относительных единицах светимости Солнца
        >>> Sun = Star('Sun', 4.603*10**9, 1.989 * 10 ** (30), 6.9634*10**8, 0, 5778)
        >>> print(Sun.luminosity())
        1.0062720420370752
        '''
        return self.energy_emitted() / self.SUN_LUMINOSITY

    def evolution(self):
        '''
        Сопоставляет диаграмму Герцшпрунга-Рассела со светимостью, температурой и размерами звезды.
        Выдает спектральный класс звезды и её дальнейшие стадии эволюции.
        :return: Спектральный класс звезды и дальнейшие стадии эволюции.
        '''
        pass


class Exoplanet(SimpleBody):
    '''
        Класс Экзопланет
    '''
    TO_EARTH_MASS_UNITS = 5.972 * 10 ** (24)
    def __init__(self, name: str, age: float, mass: float, radius: float, habitable_zone: bool,
                 temp: float, parallax: tuple, mass_au: float=None):
        '''
        Создание и подготовка к работе объекта Exoplanet
        :param name: Название экзопланеты
        :param age: Возраст экзопланеты
        :param mass: Масса экзопланеты
        :param radius: Радиус экзопланеты
        :param habitable_zone: Нахождение в обитаемой зоне
        :param temp: Средняя температура экзопланеты
        :param parallax: Паралакс экзопланеты
        :param mass_au: Масса экзопланеты в относительных единицах массы Земли

        Примеры:
        >>> Earth = Exoplanet('Earth', 4.543*10**9, 5.9742*10**24, 637100, True, 288, 0)
        '''
        super().__init__(name, age, mass, radius, temp)
        self.habitable_zone = habitable_zone
        self.parallax = parallax
        self._mass_au = mass_au
        if self.mass is None and self._mass_au is None:
            raise TypeError('Input mass in kg or a.u.')
        if self._mass_au is None:
            self._mass_au = self.mass_to_au()

    @property
    def mass_au(self):
        '''
        Делает приватный атрибут _mass_au свойством. Это необходимо потому, что масса в относительных
        единицах напрямую завязана на обычной массе и менять относительную массу без изменения обычной
        нельзя.
        :return: возвращает значение свойства mass_au

        Примеры:
        >>> Jupiter = Exoplanet('Jupiter', 4.603*10**9, 1.8987*10**27, 69.911*10**6,False, 163, (6.378*10**6,2.2))
        >>> print(Jupiter.mass_to_au())
        317.9336905559277
        >>> Jupiter.mass_au = 1
        Traceback (most recent call last):
        ...
        AttributeError: can't set attribute
        '''
        return self._mass_au

    def __repr__(self):
        '''
        Возвращает валидную питоновскую строку
        :return: Возвращает валидную питоновскую строку

        Примеры:
        >>> Jupiter = Exoplanet('Jupiter', 4.603*10**9, 1.8987*10**27, 69.911*10**6,False, 163, (6.378*10**6,2.2))
        >>> print(repr(Jupiter))
        Exoplanet(name='Jupiter', age=4.603e+09, mass=1.8987e+27, radius=69911000.0, habitable_zone=False, temp=163, parallax=(6378000.0, 2.2), mass_au=3.18e+02)
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age:.4}, mass={self.mass:.5}, " \
               f"radius={self.radius}, habitable_zone={self.habitable_zone}, temp={self.temp}, " \
               f"parallax={self.parallax}, mass_au={self._mass_au:.3})"

    def mass_to_au(self):
        '''
        Необходимость переписывания метода перевода массы из килограмм в относительные единицы для данного дочернего
        класса обусловлена тем, что сравнение параметров экзопланеты идет с Землей, а не Солнцем. Чтобы при работе
        с данным классом не приходилось видеть значения с пятью нулями после запятой, метод был перегружен.
        :return: Масса объекта в относительных единицах массы Земли

        Примеры:
        >>> Jupiter = Exoplanet('Jupiter', 4.603*10**9, 1.8987*10**27, 69.911*10**6,False, 163, (6.378*10**6,2.2))
        >>> print(Jupiter.mass_to_au())
        317.9336905559277
        '''
        return self.mass / self.TO_EARTH_MASS_UNITS

    def how_far(self) -> float:
        '''
        Метод отличается от родительского, потому что для определения расстояния до экзопланеты необходимо
        знать характеристики ближайшей звезды. Также можно использовать параллакс.
        :return: Расстояние до планеты

        Примеры:
        >>> Jupiter = Exoplanet('Jupiter', 4.603*10**9, 1.8987*10**27, 69.911*10**6,False, 163, (6.378*10**6,2.2))
        >>> print(Jupiter.how_far())
        597980424659.1892
        '''
        return self.parallax[0]/(2 * math.sin((math.radians(self.parallax[1]/3600))/2))

    def is_appropriate_for_life(self) -> float:
        '''
        Данный метод принимает на вход различные параметры такие как: масса экзопланеты в единицах
        массы земли, радиус планеты в единицах радиуса земли, нахождение в обитаемой зоне и много
        других. После чего выдается ответ в диапазоне от 0 - непригодна для жизни до 1. На данный
        момент 1 есть только у Земли.
        :return: Число в диапазоне от 0 до 1, соответствующее вероятности существования жизни
        '''
        pass


class CompoundObject(AstronomicalObject):
    '''
    Класс сложных, составных объектов
    '''

    def __init__(self, name: str, age: float, mass_au: float, redshift: float, type: str):
        '''
        Создание и подготовка к работе объекта CompoundObject
        :param name: Название масштабной структуры
        :param age: Возраст масштабной структуры
        :param mass_au: Масса масштабной структуры в относительных единицах массы Солнца
        :param redshift: Красное смещение масштабной структуры
        :param type: Тип масштабной структуры (Например планетарная система, созвездие, галактика и т.п.

        Примеры:
        >>> andromeda = CompoundObject('Andromeda', 1.001*10**10, 1.23*10**12, 0.001004, 'Galaxy')
        '''
        super().__init__(name, age, mass_au=mass_au, redshift=redshift)
        self.type = type

    @AstronomicalObject.mass_au.setter
    def mass_au(self, new_mass: float) -> None:
        '''
        Сэттер для свойства mass_au
        Необходимость в добавлении сэттера обусловлена тем, что такие массивные объекты как галактики и звездные
        скопления описываются с помощью относительных единиц масс Солнца и никто не использует киллограммы
        :param new_mass: Новое значение для свойства mass_au
        :return: Ничего не возвращает. Присваивает новое значение свойству mass_au

        Примеры:
        >>> andromeda = CompoundObject('Andromeda', 1.001*10**10, 1.23*10**12, 0.001004, 'Galaxy')
        >>> andromeda.mass_au = 'string'
        TypeError
        >>> andromeda.mass_au = -1
        ValueError
        >>> andromeda.mass_au = 1*10**10
        '''
        if not isinstance(new_mass, float):
            raise TypeError
        if new_mass < 0:
            raise ValueError
        self._mass_au = new_mass

    def __repr__(self):
        '''
        Возвращает валидную питоновскую строку
        :return: Возвращает валидную питоновскую строку

        Примеры:
        >>> andromeda = CompoundObject('Andromeda', 1.001*10**10, 1.23*10**12, 0.001004, 'Galaxy')
        >>> print(repr(andromeda))
        CompoundObject(name='Andromeda', age=1.001e+10, mass_au=1.23e+12, redshift=0.001004, type='Galaxy')
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age:.4}, " \
               f"mass_au={self._mass_au:.3}, redshift={self.redshift}, type={self.type!r})"


if __name__ == "__main__":
    doctest.testmod()
    # Sun = Star('Sun', 1, 1, 696340000, 1, 5778)
    # Earth = SimpleBody('Earth', 1, 1, 637100, 288)
    # print(Earth.mass_au)
    # print(Sun.mass_au)
    # print(Sun.energy_emitted())
    # print(Sun.luminosity())
    # print(Earth.energy_emitted())
    # andromeda = CompoundObject('Andromeda', 1.001 * 10 ** 10, 1.23 * 10 ** 12, 0.001004, 'Galaxy')
    # print(f'andromeda`s mass {andromeda.mass_au}')
    # andromeda.mass_au = 1.0
    # print(f'andromeda`s NEW mass {andromeda.mass_au}')

    # Write your solution here
    pass
