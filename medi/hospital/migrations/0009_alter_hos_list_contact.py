# Generated by Django 4.2 on 2023-05-05 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospital", "0008_alter_hos_list_hos_beds"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hos_list",
            name="contact",
            field=models.IntegerField(default=0),
        ),
    ]
