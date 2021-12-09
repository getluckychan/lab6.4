from abc import ABC, abstractmethod
import numpy as np


def read():
    n = input("Введіть массив: ")
    return np.array([int(x) for x in str(n)])


big_lst = read()


class List(ABC):

    def template_func(self):
        self.temlate_method()
        self.min_and_max()
        self.norm()
        self.sorting()


    @abstractmethod
    def temlate_method(self):
        pass

    @abstractmethod
    def min_and_max(self):
        pass

    @abstractmethod
    def norm(self):
        pass

    @abstractmethod
    def sorting(self):
        pass


class UsingTemplate(List):
    def __init__(self):
        self.lst = None

    def temlate_method(self):
        list_for = big_lst
        b = np.append(list_for[1:], 0)
        c = b[list_for != b]
        self.lst = c
        print(self.lst)

    def get_lst(self):
        return self.lst

    def min_and_max(self):
        print(np.min(self.lst), np.max(self.lst))

    def norm(self):
        print(np.linalg.norm(self.lst, ord=1))

    def sorting(self):
        print(np.sort(self.lst))


def using_template(abstract_class: List):
    abstract_class.template_func()


if __name__ == "__main__":
    print("using templates")
    print(using_template(UsingTemplate()))
