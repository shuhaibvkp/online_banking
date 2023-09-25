# Generated by Django 4.2.1 on 2023-07-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0007_ministatement'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=300)),
                ('content', models.CharField(max_length=3000)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
