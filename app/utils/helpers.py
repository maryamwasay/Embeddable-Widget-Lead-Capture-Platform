import uuid
from datetime import datetime


def generate_widget_token() -> str:
    """
    Generate a unique widget token.
    """

    return str(uuid.uuid4())


def current_timestamp():
    """
    Return current UTC timestamp.
    """

    return datetime.utcnow()


def success_response(
    message: str,
    data=None
):
    """
    Standard success response.
    """

    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(
    message: str
):
    """
    Standard error response.
    """

    return {
        "success": False,
        "message": message
    }
