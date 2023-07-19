# Generated by Django 4.2.3 on 2023-07-17 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userinfo_role_alter_userinfo_index_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='角色名称')),
            ],
            options={
                'verbose_name_plural': '角色表',
            },
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.characters', verbose_name='发布人'),
        ),
    ]
