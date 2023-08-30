# Generated by Django 4.2 on 2023-08-30 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='商品名称')),
                ('desc', models.TextField(null=True, verbose_name='商品简介')),
                ('picture', models.FileField(upload_to='goods/', verbose_name='商品封面')),
                ('orderNum', models.IntegerField(null=True, verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品价格')),
            ],
            options={
                'verbose_name_plural': '商品管理',
            },
        ),
    ]
