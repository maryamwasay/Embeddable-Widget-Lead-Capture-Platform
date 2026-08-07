from slowapi import Limiter

from slowapi.util import get_remote_address

from slowapi.errors import RateLimitExceeded

from slowapi.extension import (
    _rate_limit_exceeded_handler
)



limiter = Limiter(

    key_func=get_remote_address

)



rate_limit_exception = RateLimitExceeded


rate_limit_handler = (
    _rate_limit_exceeded_handler
)