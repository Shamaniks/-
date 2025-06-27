from abc import ABC, abstractmethod

class AbstractDatabase(ABC):
    @abstractmethod
    def find_templates(self, fields: dict[str, str]) -> list[str]: pass

