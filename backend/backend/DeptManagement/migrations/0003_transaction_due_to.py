# Generated by Django 4.0.5 on 2022-07-26 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeptManagement', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='due_to',
            field=models.DateField(default=datetime.date(2022, 7, 26)),
        ),
    ]
