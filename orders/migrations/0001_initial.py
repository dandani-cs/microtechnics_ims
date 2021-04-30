# Generated by Django 3.2 on 2021-04-30 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_num', models.CharField(default=orders.models.generate_uuid, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('project_id', models.CharField(default=orders.models.generate_uuid, max_length=10)),
                ('items', models.JSONField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('is_approved', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('approved_admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_by', to=settings.AUTH_USER_MODEL)),
                ('requested_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
