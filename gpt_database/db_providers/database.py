from abc import ABC, abstractmethod
from typing import Any


class BaseDatabase(ABC):

    @abstractmethod
    def get_schema(self) -> str:
        pass

    @abstractmethod
    def query(self, sql_query: str) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def cleanup(self):
        pass
