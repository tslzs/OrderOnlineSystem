# Generated by Django 2.1.5 on 2020-12-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0012_auto_20201219_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='picture',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='餐品图片'),
        ),
    ]
