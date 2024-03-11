import uuid
from django.db import models
from django.utils.crypto import get_random_string

from advertisement.models import Advertisement


class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_code = models.CharField(max_length=12, unique=True, default=get_random_string)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.DO_NOTHING)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    guests_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.booking_code}"
