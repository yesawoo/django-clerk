from django.db import models


class RawClerkEvent(models.Model):
    json_blob = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
