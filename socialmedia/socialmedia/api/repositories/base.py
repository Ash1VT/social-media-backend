from abc import ABC
from setup import db


class BaseRepository(ABC):

    @classmethod
    def commit(cls):
        db.session.commit()
