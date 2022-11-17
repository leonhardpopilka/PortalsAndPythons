from abc import ABC, abstractmethod


class Status(ABC):
    """An abstract class for all statuses in the game"""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def value(self) -> int:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    def is_active(self) -> bool:
        return self.value > 0

    @abstractmethod
    def reset(self):
        pass

    def __str__(self):
        return f"{self.name}: {self.value}\n{self.description}"


class Wounded(Status):

    def __init__(self, value: int):
        self._name = "Wounded"
        self._value = value
        self._description = "A wound is caused by low health and adds a negative modifier."

    @property
    def name(self) -> str:
        return "Wounded"

    @property
    def value(self) -> int:
        return self._value

    @property
    def description(self) -> str:
        return "This character is wounded and has a reduced health"

    def reset(self):
        self._value = 0
