import uuid
from django.db import models


class Property(models.Model):
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    max_guests = models.PositiveIntegerField()
    bathrooms_quantity = models.PositiveIntegerField()
    pets_allowed = models.BooleanField(default=False)
    # cleaning_fee: cents
    cleaning_fee = models.PositiveIntegerField()
    activation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)