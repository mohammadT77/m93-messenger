from abc import ABC, abstractmethod
from typing import Any, Generator


class BaseModel(ABC):
    TABLE_NAME = None
    COLUMNS = {
        '_id': ('_id', 'SERIAL', 'PRIMARY KEY'),
    }
    
    _id: int

    def __repr__(self):
        return f"<{self.__class__.__name__} #{self._id}>"
    
    @classmethod
    def from_dict(cls, data: dict):
        obj = cls.__new__(cls)
        for k, v in data.items():
            setattr(obj, k, v)
        return obj

    @classmethod
    def _get_columns(cls):
        super_cols = getattr(super(cls, cls), 'COLUMNS', {})
        cls_cols = getattr(cls, 'COLUMNS', {})
        super_cols.update(cls_cols)
        return super_cols

    def dict(self):
        result = vars(self).copy()
        for k in result.keys():
            if not k.lower():
                del result[k]
        return result

    @property
    def id(self):
        return self._id


class BaseManager:
    
    def __init__(self, config: dict) -> None:
        self._config = config or {}

    @property
    def config(self):
        return self._config

    @abstractmethod
    def create(self, m: BaseModel) -> Any:
        pass

    @abstractmethod
    def read(self, id: int, model_cls: type) -> BaseModel:
        pass

    @abstractmethod
    def update(self, m: BaseModel) -> None:
        pass

    @abstractmethod
    def delete(self, id: int, model_cls: type) -> None:
        pass

    @abstractmethod
    def read_all(self, model_cls: type = None) -> Generator:
        pass