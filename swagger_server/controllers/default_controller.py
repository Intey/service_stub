import connexion
import six

from swagger_server.models.entity import Entity  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def decreeses_post(text):  # noqa: E501
    """Получение похожих приказов

    Запрос приказов которые содержат подходящие сущности в своем шаблоне, которые подойдут для заполнения # noqa: E501

    :param text: Текст заявления
    :type text: str

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def extract_post(text):  # noqa: E501
    """Извлечение меток из заявления

    Запрос для извлечения меток из документа # noqa: E501

    :param text: Текст заявления
    :type text: str

    :rtype: List[Entity]
    """
    return 'do some magic!'
