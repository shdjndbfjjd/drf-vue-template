# Generated by Django 4.2 on 2023-09-06 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_goodsspecs_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsspecs',
            name='spec_type',
            field=models.IntegerField(choices=[(1, '颜色'), (2, '尺码')], null=True, verbose_name='规格类型'),
        ),
        migrations.CreateModel(
            name='ShopDetailImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='shop_detail/', verbose_name='商品详情图片')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='对应商品')),
            ],
            options={
                'verbose_name_plural': '商品详情图片',
            },
        ),
    ]
