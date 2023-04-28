from .base import BaseModel, BaseManager
from typing import Generator, Any 
import pickle
import os

class FileManager(BaseManager):

    def __init__(self, config: dict) -> None:
        super().__init__(config)
        self._files_root = config.get('ROOT_PATH') # data/

    def _get_id(self, model_type: type) -> int: # User
        files = os.listdir(self._files_root+'/')
        ids = []
        for f in files:
            if f.startswith(model_type.__name__):
                ids.append(int(f.split('_')[-1].split('.')[0]))
        return max(ids)+1 if ids else 1

    def _get_file_path(self, _id, model_type: type) -> str:
        return f"{self._files_root}/{model_type.__name__}_{_id}.pkl".replace('//', '/')

    def create(self, m: BaseModel) -> Any:   # manager.create(user) # user.id!!!!
        m._id = self._get_id(m.__class__)  # set ID!!!!!
        path = self._get_file_path(m._id, m.__class__)
        with open(path, 'xb') as f:
            pickle.dump(m, f)
        return path
        

    def read(self, id: int, model_cls: type) -> BaseModel:
        path = self._get_file_path(id, model_cls)
        with open(path, 'rb') as f:
            m = pickle.load(f)
            return m

    def update(self, m: BaseModel) -> None:
        assert getattr(m, '_id', None), "Model does NOT have `_id`"
        path = self._get_file_path(m._id, m.__class__)
        with open(path, 'wb') as f:
            pickle.dump(m, f)
        return path

    def delete(self, id: int, model_cls: type) -> None:
        path = self._get_file_path(id, model_cls)
        if os.path.exists(path):
            os.remove(path)

    def read_all(self, model_cls: type = None) -> Generator:
        for file_name in os.listdir(self._files_root):
            if not file_name.endswith('.pkl'):
                continue
            if model_cls and not file_name.startswith(model_cls.__name__):
                continue
            file_path = os.path.join(self._files_root, file_name)
            with open(file_path, 'rb') as f:
                instance = pickle.load(f)
                if not model_cls or isinstance(instance, model_cls):
                    yield instance
