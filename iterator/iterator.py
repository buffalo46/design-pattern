from abc import ABCMeta, abstractclassmethod

class Iterator(metaclass=ABCMeta):

    @abstractclassmethod
    def has_next(self) -> bool:
        pass

    @abstractclassmethod
    def next(self):
        pass

class IteratorIF():
    pass