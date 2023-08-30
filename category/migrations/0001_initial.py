# Generated by Django 4.2 on 2023-08-30 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='分类名称')),
                ('picture', models.FileField(upload_to='category/', verbose_name='分类图片')),
                ('goods', models.ManyToManyField(to='goods.goods', verbose_name='分类商品')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='父分类')),
            ],
            options={
                'verbose_name_plural': '分类管理',
            },
        ),
    ]
