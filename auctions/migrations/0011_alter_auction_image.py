# Generated by Django 4.1 on 2023-01-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(null=b'I01\n', upload_to='media'),
        ),
    ]