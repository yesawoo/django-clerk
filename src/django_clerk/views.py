from django_clerk.models import RawClerkEvent
from django.http import HttpResponse
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from svix.webhooks import Webhook, WebhookVerificationError

import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def clerk_webhook_handler(request):
    logger.info("Received Clerk Webhook")
    headers = request.headers
    payload = request.body

    try:
        wh = Webhook(settings.CLERK_WEBHOOK_SECRET)
        msg = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        return HttpResponse(status=400)

    RawClerkEvent.objects.create(json_blob=msg)

    return HttpResponse(status=204)
