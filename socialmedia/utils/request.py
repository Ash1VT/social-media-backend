from typing import Optional, Dict

from flask import Request
from ..errors import RequestInvalidContentTypeError


def check_request_content_type(request: Request) -> Optional[Dict]:
    content_type = get_request_content_type(request=request)
    if content_type == 'multipart/form-data':
        return request.form.to_dict()
    if content_type == 'application/json':
        return request.json

    raise RequestInvalidContentTypeError()


def get_request_content_type(request: Request) -> str:
    try:
        return request.content_type.split(' ')[0].strip(';. !?:')
    except AttributeError:
        raise RequestInvalidContentTypeError()
