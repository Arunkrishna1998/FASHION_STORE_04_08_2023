# Generated by Django 4.2.3 on 2023-07-28 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_alter_guest_guest_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='guest',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
