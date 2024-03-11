import uuid
from django.db import models
from property.models import Property

class Advertisement(models.Model):
    advertisement_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    platform_name = models.CharField(max_length=100)
    # platform_tax: cents
    platform_tax = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)