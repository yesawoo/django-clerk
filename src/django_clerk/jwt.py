import json
import logging
from functools import cache
from urllib.request import urlopen

import jwt
from django.conf import settings

logger = logging.getLogger(__name__)


@cache
def get_public_keys():
    # Update this to 'https://{clerk_frontend_api}/.well-known/jwks.json'
    # Note: The content of this endpoint will never change, so it should
    # be cached on the server instead of requested with each API call
    url = settings.CLERK_JWT_JWKS_URL
    response = urlopen(url)
    data_json = json.loads(response.read())
    logger.debug(f"jwks url response: {data_json}")
    logger.debug(f"JWT Keys: {data_json['keys']}")
    return data_json['keys']


def validate(token: str):
    try:
        data = decode(token)
        logger.debug(f"Data {data}")
    except jwt.exceptions.PyJWTError as e:
        logger.error(f"JWT decoding error: {e}")
        return False

    return bool(data)


def decode(token: str):
    logger.debug(f"Decoding token {token}")
    return jwt.decode(
        token,
        key=settings.CLERK_JWT_PEM_PUBLIC_KEY,
        algorithms=["RS256"],
    )
