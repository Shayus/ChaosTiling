from django.db import models


class AppShaderBc(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'app_shader_bc'


class AppShaderD(models.Model):
    id = models.IntegerField(primary_key=True)
    fshader_d = models.TextField()

    class Meta:
        managed = False
        db_table = 'app_shader_d'


class AppShaderG(models.Model):
    id = models.IntegerField(primary_key=True)
    fshader_g = models.TextField()
    discribe = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255)
    num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_shader_g'


class AppShaderJ(models.Model):
    id = models.IntegerField(primary_key=True)
    fshader_j = models.TextField()
    discribe = models.CharField(max_length=255, blank=True, null=True)
    extra = models.IntegerField()
    path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'app_shader_j'


class AppShaderMain(models.Model):
    id = models.IntegerField(primary_key=True)
    fshader_unit = models.TextField()
    fshader_main = models.TextField()
    discribe = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_shader_main'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'