# Generated by Django 4.2.1 on 2023-07-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0003_regmodel1_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='regmodel1',
            name='account',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
