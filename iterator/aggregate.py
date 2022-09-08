import abc

from ..common.model import Interface
from .iterator import IteratorIF

class AggregateIF(Interface):
    @abc.abstractclassmethod
    def iterator(self) -> IteratorIF:
        pass
    