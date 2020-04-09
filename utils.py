import random
import time
import os
from logging import getLogger
from io import BytesIO

from PIL import Image


def debug_requests(f):
    """ Декоратор для отладки событий от телеграма
        Логгер подключается в самый последний момент чтобы быть уверенными в том, что конфиг логирования уже загружен
    """
    from logging import getLogger
    logger = getLogger(__name__)

    def inner(*args, **kwargs):
        try:
            logger.debug('Обращение в функцию {}'.format(f.__name__))
            return f(*args, **kwargs)
        except Exception:
            logger.exception('Ошибка в обработчике {}'.format(f.__name__))
            raise

    return inner