# Generated by Django 4.1.5 on 2023-03-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_evacuationmsg_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evacuationmsg',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='evacuationmsg',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
