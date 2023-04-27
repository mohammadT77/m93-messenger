from .base import BaseModel, BaseManager
from typing import Generator, Any 
import pickle
import os


class FileManager(BaseManager):

    def __init__(self, config: dict) -> None:
        self._files_root = config.get('ROOT_PATH')  # data/

    def _get_id(self, model_type: type) -> int:  # User
        files = os.listdir(self._files_root+'/')
        ids = []
        files = filter(lambda file_name: file_name.startswith(model_type.__name__), files)
        ids = list(map(lambda file_name: int(file_name.split('.')[0].split('_')[-1]), files))
        return max(ids)+1 if ids else 1

    def _get_file_path(self, _id, model_type: type) -> str:
        return f"{self._files_root}/{model_type.__name__}_{_id}.pkl".replace('//', '/')

    def create(self, m: BaseModel) -> Any:   # manager.create(user) # user.id!!!!
        m._id = self._get_id(m)  # set ID!!!!!
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
        path = self._get_file_path(m._id, m.__class__)
        with open(path, 'wb') as f:
            pickle.dump(m, f)

    def delete(self, id: int, model_cls: type) -> None:
        path = self._get_file_path(id, model_cls)
        if os.path.exists(path):
            os.remove(path)

    def read_all(self, model_cls: type = None) -> Generator:
        pass
