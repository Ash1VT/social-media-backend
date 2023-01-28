from typing import Dict

from socialmedia.constants import REQUEST_INVALID_CONTENT_TYPE_ERROR_STRING, DEFAULT_ERROR_RESPONSE

__all__ = ['get_request_invalid_content_type_response_body']


def get_request_invalid_content_type_response_body() -> Dict:
    return {
        **DEFAULT_ERROR_RESPONSE,
        'message': REQUEST_INVALID_CONTENT_TYPE_ERROR_STRING
    }
