import logging
from django.contrib.auth import get_user_model

from .jwt import decode, validate

User = get_user_model()
logger = logging.getLogger(__name__)


class ClerkMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request = self.process_request(request)
        response = self.get_response(request)
        request = self.process_response(request, response)

        return response

    def process_request(self, request):
        token = self.get_auth_token(request)
        if token and self.validate_token(token):
            request.user = self.get_user_from_token(token)
            logger.debug(f"Request User: {request.user}")
        else:
            request.user = None
        return request

    def process_response(self, request, response):
        return response

    def get_auth_token(self, request):
        return request.headers.get("Authorization", "").split("Bearer ")[-1]

    def validate_token(self, token):
        return validate(token)

    def get_user_from_token(self, token):
        """
        Retrieves a user object based on the provided token.
        This method can be overridden to customize the user 
        retrieval process.

        Args:
            token (str): The token used to identify the user.

        Returns:
            User: The user object associated with the token. If
            the user does not exist, a new user object will be created.
        """
        data = decode(token)
        if User.objects.filter(email=data["email"]).exists():
            user = User.objects.get(email=data["email"])
        else:
            user = User.objects.create(email=data["email"])

        return user
