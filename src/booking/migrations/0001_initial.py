# Generated by Django 4.2 on 2024-03-11 05:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisement', '0002_remove_advertisement_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('booking_code', models.CharField(default=django.utils.crypto.get_random_string, max_length=12, unique=True)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('total_price', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('guests_count', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='advertisement.advertisement')),
            ],
        ),
    ]