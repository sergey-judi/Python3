def str_to_dict(some_str):  
    """
    :param some_str: str
    :return: dict
    """
    # YOUR CODE HERE
    count_dict = dict()
    for letter in some_str:
        if not (letter in count_dict.keys()):
            count_dict[letter] = some_str.count(letter)
    return count_dict


# print('Str to dict:', str_to_dict('dataroot_university'))


def sec_smallest(numbers):
    """
    :param numbers: list[int]
    :return: int    
    """
    minimum = min(numbers)
    sec_minimum = max(numbers)

    for number in numbers:
        if number < sec_minimum and number != minimum:
            sec_minimum = number
    
    return sec_minimum


# print('Sec_smallest:', sec_smallest([1, 2, -8, -8, -2, 0]))


def prime_nums(n):
    """
    :param n: int
    :return: list[int]
    """
    primes = list()
    if n <= 1:
        return primes
    i = 2
    primes.append(i)
    while i <= n:
        if not any(map(lambda x: i % x == 0, primes)):
            primes.append(i)
        i += 1
    return primes


# print('Prime numbers:', prime_nums(30))


def max_sum_index(tuples):
    '''
    :param tuples: list[tuple]
    :return: int
    '''
    max_sum = -float('inf')
    index = -1

    for i, numbers in enumerate(tuples):
        if sum(numbers) > max_sum:
            max_sum = sum(numbers)
            index = i
    return index


# print(max_sum_index([(10, 20), (40, 32), (30, 25)]))


def gcd(x, y):
    '''
    :params m,n: int
    :return: int
    '''
    if x == 0:
        return y
    if y == 0:
        return x
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


# print(gcd(160, 180))
# print(gcd(1071, 462))
# print(gcd(0, 3))


def recursive_list_sum(data_list):
    """
    :param data_list: list[list]
    """
    list_sum = 0
    for entity in data_list:
        if isinstance(entity, list):
            list_sum += recursive_list_sum(entity)
        else:
            list_sum += entity
    return list_sum


# print('The sum of a list is ', recursive_list_sum([1, 2, [3,4],[5,6], [7, 8, 9]]))


def debug(func):
    """
    :param func: function
    """
    def decorator(*args):
        print(func.__name__ + str(args) + ' was called and returned ' + str(func(*args)))
        return func(*args)
    return decorator


@debug
def add(a, b):
    return a + b


# add(3, 4)


class Conv:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        self.syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]

    def to_roman(self, num):
        """
        :param self:
        :param num: int
        :return: str
        """
        roman_string = ''
        accum = 0
        k = 0
        i = 10
        # while (rest := ((num - accum) % i)) != 0:
        while k != len(str(num)):
            temp_string = ''
            rest = (num - accum) % i
            print(rest)
            if rest in self.val:
                symbol_index = self.val.index(rest)
                temp_string += self.syb[symbol_index]
            else:
                temp_rest = rest

                while not(temp_rest in self.val):
                    symbol_index = self.val.index(1)
                    temp_string += self.syb[symbol_index]
                    temp_rest -= 1

                symbol_index = self.val.index(temp_rest)
                temp_string = self.syb[symbol_index] + temp_string

            roman_string = temp_string + roman_string
            i *= 10
            k += 1
            accum += rest
        return roman_string


# print('Converted:', Conv().to_roman(158))


class CombinationsList:
    @staticmethod
    def get_combinations(my_list):
        """
        :param self:
        :param my_list: list
        :return: list[list]
        """
        from itertools import combinations
        combinations_list = list()
        for i in range(len(my_list)+1):
            combinations_list.extend(map(list, combinations(my_list, i)))
        return combinations_list


# print('Combinations:', CombinationsList().get_combinations([1, 2, 'a']))


class Rocket:

    def __init__(self, name, mission):
        """
        :param name: str
        :param mission: str or list
        """
        # attributes are private to class Rocket
        self.__name = name
        self.__mission = mission

    def getMission(self):
        """
        :return str or list
        """
        return self.__mission

    def addMission(self, mission):
        # procedure method which adds a new mission. There can be one (str) or multiple (list) existing missions
        """
        :param mission: str
        """
        if isinstance(self.__mission, list):
            self.__mission.append(mission)
        else:
            self.__mission = [self.__mission]
            self.__mission.append(mission)

    def getName(self):
        """
        :return str
        """
        return self.__name


class Shuttle(Rocket):

    def __init__(self, name, mission, model):
        # call parent constructor to set name and mission
        """
        :param name: str
        :param mission: str or list
        :param model: str
        """
        super().__init__(name, mission)
        self.__model = model

    def getDescription(self):
        return 'Name: {0}\nModel: {1}\nMissions: {2}'.format(self.getName(), self.__model, str(self.getMission()))


# dragon = Shuttle("Crew Dragon", "Dragon 2 pad abort test", "V2")
# print(dragon.getDescription(), '\n')
# dragon.addMission('Dragon 2 in-flight abort test')
# print(dragon.getDescription())
