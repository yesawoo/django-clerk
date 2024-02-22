import logging
from django.contrib.auth import get_user_model

from .jwt import decode, validate

User = get_user_model()
logger = logging.getLogger(__name__)


class ClerkMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = self.get_auth_token(request)
        if token and self.validate_token(token):
            request.user = self.get_user_from_token(token)
            logger.debug(f"Request User: {request.user}")
        else:
            request.user = None

        ###
        response = self.get_response(request)
        ###

        return response

    def get_auth_token(self, request):
        return request.headers.get("Authorization", "").split("Bearer ")[-1]

    def validate_token(self, token):
        return validate(token)

    def get_user_from_token(self, token):
        data = decode(token)
        return User.objects.get(email=data["email"])
