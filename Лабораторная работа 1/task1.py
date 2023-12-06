import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class CertesianSystem:
    def __init__(self, num_axis: int, metric: str):
        """
        создание объекта "CertesianSystem" (декартова система координат)
         и заполнение его атрибутов:

         :param num_axis: размерность системы координат
         :param metric: метрика, используемая для подсчета расстояний

        Пример:
        >>> CS1 = CertesianSystem(3, 'м')

        """
        if not isinstance(num_axis, int):
            raise TypeError('num_axis must be int')

        self.metric = None

        self.num_axis = num_axis
        self.points = []

        self.define_metric(metric)

#метрика проверяется и назначается на в __init__ так как эта же функция
#может использоваться для назначения метрики пользователем отдельно -> экономия кода
    def define_metric(self, metric: str):
        """
        Назначает метрику при создании объекта класса.
        Может быть вызван пользователем для изменения метрики.

        :param metric: назначаемая метрика

        :raise TypeError: если metric not in list

        :raise ValueError: если количество координат точки не совпадает с
        количеством координатных осей данной системы
        """
        if metric in ['м', 'см', 'мм']:
            self.metric = metric
        else:
            raise TypeError('unknown metric')

    def create_point(self, coordinates: tuple):
        if not isinstance(coordinates, tuple):
            raise TypeError('coordinates must be tuple')

        if len(coordinates) != self.num_axis:
            self.points.append(coordinates)
        else:
            raise ValueError('vector dimensions not equal to system dimensions')
        ...

    def get_info(self) -> (int, str, list):
        """
        возвращает информацию об атрибутах объекта

        :return: кортеж атрибутов
        """

        return self.num_axis, self.metric, self.points


class Player:
    def __init__(self, position: tuple):
        """
        создание объекта Player и задание атрибутов

        :param position: Текущая позиция игрока

        Пример:
        >>> player = Player((0, 0, 0))
        """
        if not isinstance(position, tuple):
            raise TypeError('positnion must be tuple')
        self.position = position
        self.score = 0
        self.HP = 100
        self.MP = 50
        self.lvl = 1

        self.alive = True

    def update_score(self, add_score: float):
        """
        обновление счета игрока

        :param add_score: количество добавляемых очков
        """
        if not isinstance(add_score, float):
            raise TypeError('add_score is not float')
        ...

    def is_alive(self) -> bool:
        """
        позволяет проверить жив ли игрок в данный момент

        :return: True если игрок жив, False если мертв

        Пример:
        >>> player = Player((0, 0, 0))
        >>> player.is_alive()
        True
        """
        return self.alive

    def change_position(self, position_changes: tuple, teleportation = False):
        """
        позволяет изменить позицию игрока

        :param position_changes: изменения координат. Кортеж трех чисел.

        :param teleportation: Если False то добавляем position_changes к текущим координатам.
        Если True, то заменяем текущие координаты на position_changes
        """
        if isinstance(position_changes, tuple):
            if len(position_changes) != 3:
                raise TypeError('len of position_changes must be equal 3')
        else:
            raise TypeError('position_changes is not tuple')
        ...

class Organization:
    def __init__(self, budget: float,
                 workers: list[tuple[str, int, int]],
                 blacklist: list[tuple[str, int]]):
        """
        Создание компании и заполнение информации о ней

        :param budget: стартовый бюджет компании

        :param workers: список работников компании. Имет вид
        list[tuple[ФИО, паспорт, ID в компании]]

        :param blacklist: черный список людей компании. Этих людей компания
        не примет на работу и не окажет им услуги. Имеет вид
        list[tuple[ФИО, паспорт]]
        """

        if not isinstance(budget, (float, int)):
            raise TypeError('budget must be float or int')
        if budget < 0:
            raise ValueError('budget must be grater than 0')
        self.budget = budget

        if len(workers) < 1:
            raise ValueError('amount of workers must be grater that 1')
        self.workers = workers
        self.blacklist = blacklist

    def in_blacklist(self, person: int) -> bool:
        """
        проверяет на наличие в self.blacklist

        :param person: паспорт человека, которого требуется проверить
         на наличие в черном списке

        :return: True если person в черном списке, Flase если нет
        """
        if not isinstance(person, int):
            raise TypeError("person must be int")
        ...

    def new_worker(self, worker: tuple[str, int]) -> bool:
        """
        Заносит человека в базу данных работников компании.
        Если человек в черном списке компании - отклоняет запрос о внесении в БД.

        :param worker: ФИО и паспорт человека, которого требуется принять на работу.

        :return: True если человек принят на работу,
        False если запрос отклонен и человек не занесен в БД
        """
        if not isinstance(worker, list):
            raise TypeError('worker must be tuple')

        if self.in_blacklist(worker[1]):
            return False
        else:
            ...
            return True

    def pay_taxes(self, cost: float):
        """
        метод для уплаты налогов

        :param cost: сумма к уплате

        :return: False если в бюджете недостаточно денег для уплаты,
        True если налог заплачен успешно.
        """
        if not isinstance(cost, (int, float)):
            raise TypeError('cost must be int or float')

        if cost > self.budget:
            # print('вы банкрот')
            # del self
            return False
        else:
            ...
            return True


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
