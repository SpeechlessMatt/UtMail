from .utmail import UtMail
from .utmail import Api
from . import __path__
import os

# 额外的模块目录 Api
Api_path = os.path.join(os.path.dirname(__file__), 'api')
__path__.append(Api_path)


__version__ = "0.1.6"

__all__ = [
    "UtMail",
    "Api",
    "ChacuoOption"
]


