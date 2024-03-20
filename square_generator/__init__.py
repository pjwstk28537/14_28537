from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @abstractmethod
    def e_squares(self, begin, end):
        pass
