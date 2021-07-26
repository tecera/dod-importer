from abc import ABC, abstractmethod


class BaseCharacter(ABC):
    def __str__(self):
        return str(self.dict())

    @abstractmethod
    def dict(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.dict() == other.dict()
