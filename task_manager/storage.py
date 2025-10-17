from __future__ import annotations


class InMemoryStorage:
    def __init__(self):
        # usar dicionário interno simples
        self._data: dict[int, object] = {}

    def add(self, id: int, item: object) -> None:
        self._data[id] = item

    def get(self, id: int):
        return self._data.get(id)

    def get_all(self):
        return list(self._data.values())

    def delete(self, id: int) -> bool:
        if id in self._data:
            del self._data[id]
            return True
        return False

    def clear(self) -> None:
        self._data.clear()
