# Generated by Django 3.0.4 on 2020-03-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppShaderBc',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'app_shader_bc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppShaderColor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fshader_color_set', models.TextField()),
            ],
            options={
                'db_table': 'app_shader_color',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppShaderG',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fshader_g', models.TextField()),
            ],
            options={
                'db_table': 'app_shader_g',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppShaderJ',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fshader_j', models.TextField()),
            ],
            options={
                'db_table': 'app_shader_j',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppShaderMain',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fshader_main', models.TextField()),
            ],
            options={
                'db_table': 'app_shader_main',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AppShaderUnit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fshader_unit', models.TextField()),
            ],
            options={
                'db_table': 'app_shader_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
    ]
