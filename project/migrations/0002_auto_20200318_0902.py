# Generated by Django 3.0.4 on 2020-03-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppShaderD',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fshader_d', models.TextField()),
            ],
            options={
                'db_table': 'app_shader_d',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AppShaderUnit',
        ),
    ]
