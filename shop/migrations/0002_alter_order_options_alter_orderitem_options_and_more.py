# Generated by Django 4.2.1 on 2023-06-20 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pk']},
        ),
    ]
