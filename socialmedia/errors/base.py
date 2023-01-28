from abc import ABC, abstractmethod
from typing import Tuple

from flask import Response

__all__ = ['AppError']


class AppError(Exception, ABC):
    """Base error class in application"""

    @property
    @abstractmethod
    def response(self) -> Tuple[Response, int]:
        pass
