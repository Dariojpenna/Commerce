# Generated by Django 4.1 on 2023-01-12 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_auction_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bid', to='auctions.bid'),
        ),
    ]
