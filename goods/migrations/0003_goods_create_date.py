# Generated by Django 4.2 on 2023-09-01 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_goods_ordernum'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间'),
        ),
    ]
