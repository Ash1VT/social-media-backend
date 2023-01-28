from abc import ABC
from setup import db

__all__ = ['BaseRepository']


class BaseRepository(ABC):

    @classmethod
    def commit(cls):
        db.session.commit()
