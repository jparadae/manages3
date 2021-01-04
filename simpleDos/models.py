# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Accion(models.Model):
    nombre = models.CharField(max_length=128)
    tipo = models.CharField(max_length=32)
    extra = models.TextField(blank=True, null=True)
    proceso = models.ForeignKey('Proceso', models.DO_NOTHING)
    exponer_variable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accion'


class Acontecimiento(models.Model):
    estado = models.IntegerField()
    evento_externo = models.ForeignKey('EventoExterno', models.DO_NOTHING)
    etapa = models.ForeignKey('Etapa', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'acontecimiento'


class Anuncio(models.Model):
    texto = models.CharField(max_length=255)
    tipo = models.CharField(max_length=11, blank=True, null=True)
    activo = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anuncio'


class AuditoriaOperaciones(models.Model):
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=512, blank=True, null=True)
    detalles = models.TextField()
    operacion = models.CharField(max_length=128, blank=True, null=True)
    usuario = models.CharField(max_length=390)
    proceso = models.CharField(max_length=128)
    cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auditoria_operaciones'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Campo(models.Model):
    nombre = models.CharField(max_length=32)
    readonly = models.IntegerField()
    valor_default = models.TextField()
    posicion = models.PositiveIntegerField()
    tipo = models.CharField(max_length=32)
    formulario = models.ForeignKey('Formulario', models.DO_NOTHING)
    etiqueta = models.TextField()
    ayuda = models.TextField()
    validacion = models.CharField(max_length=128)
    dependiente_tipo = models.CharField(max_length=7)
    dependiente_campo = models.CharField(max_length=64, blank=True, null=True)
    dependiente_valor = models.CharField(max_length=256, blank=True, null=True)
    datos = models.TextField(blank=True, null=True)
    documento = models.ForeignKey('Documento', models.DO_NOTHING, blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    dependiente_relacion = models.CharField(max_length=2)
    condiciones_extra_visible = models.TextField(blank=True, null=True)
    agenda_campo = models.BigIntegerField(blank=True, null=True)
    exponer_campo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'campo'


class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=256)
    icon_ref = models.CharField(max_length=256, blank=True, null=True)
    cuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class ColaContinuarTramite(models.Model):
    tramite_id = models.IntegerField(blank=True, null=True)
    tarea_id = models.IntegerField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    procesado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cola_continuar_tramite'


class Conexion(models.Model):
    tarea_id_origen = models.ForeignKey('Tarea', models.DO_NOTHING, db_column='tarea_id_origen')
    tarea_id_destino = models.ForeignKey('Tarea', models.DO_NOTHING, db_column='tarea_id_destino',related_name='tarea_id_destino_set', blank=True, null=True)
    tipo = models.CharField(max_length=19)
    regla = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conexion'
        unique_together = (('tarea_id_origen', 'tarea_id_destino'),)


class Config(models.Model):
    idpar = models.PositiveIntegerField()
    endpoint = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    nombre_visible = models.CharField(max_length=50, blank=True, null=True)
    cuenta_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class ConfigGeneral(models.Model):
    componente = models.CharField(primary_key=True, max_length=45)
    cuenta = models.IntegerField()
    llave = models.CharField(max_length=80)
    valor = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_general'
        unique_together = (('componente', 'cuenta', 'llave'),)


class Cuenta(models.Model):
    nombre = models.CharField(unique=True, max_length=128)
    nombre_largo = models.CharField(max_length=256)
    metadata = models.TextField(blank=True, null=True)
    mensaje = models.TextField()
    logo = models.CharField(max_length=128, blank=True, null=True)
    logof = models.CharField(max_length=128, blank=True, null=True)
    favicon = models.CharField(max_length=128, blank=True, null=True)
    api_token = models.CharField(max_length=32, blank=True, null=True)
    descarga_masiva = models.IntegerField()
    client_id = models.CharField(max_length=64, blank=True, null=True)
    client_secret = models.CharField(max_length=64, blank=True, null=True)
    ambiente = models.CharField(max_length=255)
    vinculo_produccion = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    entidad = models.CharField(max_length=256, blank=True, null=True)
    estilo = models.CharField(max_length=50)
    header = models.CharField(max_length=64)
    footer = models.CharField(max_length=64)
    personalizacion = models.TextField(blank=True, null=True)
    personalizacion_estado = models.CharField(max_length=1)
    seo_tags = models.CharField(max_length=4096, blank=True, null=True)
    analytics = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


class CuentaHasConfig(models.Model):
    idpar = models.PositiveIntegerField()
    config_id = models.PositiveIntegerField()
    cuenta_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta_has_config'


class DatoSeguimiento(models.Model):
    nombre = models.CharField(max_length=128)
    valor = models.TextField()
    etapa = models.ForeignKey('Etapa', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dato_seguimiento'
        unique_together = (('nombre', 'etapa'),)


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


class Documento(models.Model):
    tipo = models.CharField(max_length=11)
    nombre = models.CharField(max_length=128)
    contenido = models.TextField()
    servicio = models.CharField(max_length=128)
    servicio_url = models.CharField(max_length=128)
    logo = models.CharField(max_length=256)
    timbre = models.CharField(max_length=256)
    sello_agua = models.CharField(max_length=255, blank=True, null=True)
    firmador_nombre = models.CharField(max_length=128)
    firmador_cargo = models.CharField(max_length=128)
    firmador_servicio = models.CharField(max_length=128)
    firmador_imagen = models.CharField(max_length=256)
    validez = models.PositiveIntegerField(blank=True, null=True)
    hsm_configuracion = models.ForeignKey('HsmConfiguracion', models.DO_NOTHING, blank=True, null=True)
    proceso = models.ForeignKey('Proceso', models.DO_NOTHING)
    subtitulo = models.CharField(max_length=128)
    titulo = models.CharField(max_length=128)
    validez_habiles = models.IntegerField(blank=True, null=True)
    tamano = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'


class Etapa(models.Model):
    tarea = models.ForeignKey('Tarea', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, blank=True, null=True)
    pendiente = models.IntegerField()
    etapa_ancestro_split = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    vencimiento_at = models.DateField(blank=True, null=True)
    vencimiento_avance = models.CharField(max_length=9, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    tramite = models.ForeignKey('Tramite', models.DO_NOTHING)
    extra = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etapa'


class Evento(models.Model):
    regla = models.CharField(max_length=512, blank=True, null=True)
    instante = models.CharField(max_length=7)
    tarea = models.ForeignKey('Tarea', models.DO_NOTHING)
    accion = models.ForeignKey(Accion, models.DO_NOTHING)
    paso = models.ForeignKey('Paso', models.DO_NOTHING, blank=True, null=True)
    evento_externo = models.ForeignKey('EventoExterno', models.DO_NOTHING, blank=True, null=True)
    campo_asociado = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'


class EventoExterno(models.Model):
    nombre = models.CharField(max_length=128)
    metodo = models.CharField(max_length=4, blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    regla = models.TextField(blank=True, null=True)
    tarea = models.ForeignKey('Tarea', models.DO_NOTHING)
    opciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento_externo'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Feriado(models.Model):
    fecha = models.DateField(unique=True)

    class Meta:
        managed = False
        db_table = 'feriado'


class File(models.Model):
    filename = models.CharField(max_length=255)
    tipo = models.CharField(max_length=9, blank=True, null=True)
    llave = models.CharField(max_length=12)
    llave_copia = models.CharField(max_length=40, blank=True, null=True)
    llave_firma = models.CharField(max_length=12, blank=True, null=True)
    validez = models.PositiveIntegerField(blank=True, null=True)
    tramite = models.ForeignKey('Tramite', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    validez_habiles = models.IntegerField(blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    campo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file'
        unique_together = (('tipo', 'tramite', 'filename'),)


class Formulario(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField(blank=True, null=True)
    proceso = models.ForeignKey('Proceso', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'formulario'


class GrupoUsuarios(models.Model):
    nombre = models.CharField(max_length=128)
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'grupo_usuarios'
        unique_together = (('cuenta', 'nombre'),)


class GrupoUsuariosHasUsuario(models.Model):
    grupo_usuarios = models.OneToOneField(GrupoUsuarios, models.DO_NOTHING, primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'grupo_usuarios_has_usuario'
        unique_together = (('grupo_usuarios', 'usuario'),)


class HistorialConsulta(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    file = models.ForeignKey(File, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial_consulta'


class HistorialModificacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    proceso = models.ForeignKey('Proceso', models.DO_NOTHING)
    usuario = models.ForeignKey('UsuarioBackend', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'historial_modificacion'


class HsmConfiguracion(models.Model):
    rut = models.PositiveIntegerField()
    nombre = models.CharField(max_length=128)
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING)
    entidad = models.CharField(max_length=256, blank=True, null=True)
    proposito = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'hsm_configuracion'
        unique_together = (('rut', 'cuenta', 'proposito'),)


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField()
    user_type = models.CharField(max_length=8)
    extra = models.TextField(blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    arguments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    downloads = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class LoginErroneo(models.Model):
    usuario = models.CharField(max_length=128)
    horario = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_erroneo'


class MensajeBackend(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensaje_backend'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Paso(models.Model):
    orden = models.PositiveIntegerField()
    modo = models.CharField(max_length=13)
    regla = models.CharField(max_length=512, blank=True, null=True)
    formulario = models.ForeignKey(Formulario, models.DO_NOTHING)
    tarea = models.ForeignKey('Tarea', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'paso'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Proceso(models.Model):
    nombre = models.CharField(max_length=128, blank=True, null=True)
    #nombre_frontend = models.CharField(max_length=255, blank=True, null=True)
    #codigo_rnt = models.CharField(max_length=128, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    url_informativa = models.CharField(max_length=255, blank=True, null=True)
    usuario = models.ForeignKey('UsuarioBackend', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    width = models.CharField(max_length=8)
    height = models.CharField(max_length=8)
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING)
    proc_cont = models.IntegerField(blank=True, null=True)
    activo = models.IntegerField()
    categoria_id = models.PositiveIntegerField(blank=True, null=True)
    destacado = models.IntegerField(blank=True, null=True)
    icon_ref = models.CharField(max_length=256, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    root = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=255)
    concurrente = models.IntegerField(blank=True, null=True)
    eliminar_tramites = models.IntegerField(blank=True, null=True)
    ocultar_front = models.IntegerField(blank=True, null=True)
    ficha_informativa = models.IntegerField()
    ficha_titulo = models.CharField(max_length=128, blank=True, null=True)
    ficha_contenido = models.TextField(blank=True, null=True)
    #descarga_documentos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proceso'


class ProcesoCuenta(models.Model):
    id_cuenta_origen = models.IntegerField(blank=True, null=True)
    id_cuenta_destino = models.IntegerField(blank=True, null=True)
    id_proceso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proceso_cuenta'


class Reporte(models.Model):
    nombre = models.CharField(max_length=128)
    campos = models.TextField()
    proceso = models.ForeignKey(Proceso, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reporte'


class Seguridad(models.Model):
    institucion = models.CharField(max_length=128, blank=True, null=True)
    servicio = models.CharField(max_length=128, blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    proceso_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguridad'


class Suscriptor(models.Model):
    institucion = models.CharField(max_length=128, blank=True, null=True)
    extra = models.TextField(blank=True, null=True)
    proceso_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suscriptor'


class Tarea(models.Model):
    identificador = models.CharField(max_length=32)
    inicial = models.IntegerField()
    nombre = models.CharField(max_length=128)
    posx = models.PositiveIntegerField()
    posy = models.PositiveIntegerField()
    asignacion = models.CharField(max_length=12)
    asignacion_usuario = models.CharField(max_length=128, blank=True, null=True)
    asignacion_notificar = models.IntegerField()
    proceso = models.ForeignKey(Proceso, models.DO_NOTHING)
    almacenar_usuario = models.IntegerField()
    almacenar_usuario_variable = models.CharField(max_length=128, blank=True, null=True)
    acceso_modo = models.CharField(max_length=15)
    activacion = models.CharField(max_length=12)
    activacion_inicio = models.DateField(blank=True, null=True)
    activacion_fin = models.DateField(blank=True, null=True)
    vencimiento = models.IntegerField()
    vencimiento_valor = models.CharField(max_length=128)
    vencimiento_unidad = models.CharField(max_length=1)
    vencimiento_habiles = models.IntegerField()
    vencimiento_notificar = models.IntegerField()
    vencimiento_notificar_email = models.CharField(max_length=255, blank=True, null=True)
    vencimiento_notificar_dias = models.PositiveIntegerField()
    grupos_usuarios = models.TextField(blank=True, null=True)
    paso_confirmacion = models.IntegerField()
    paso_confirmacion_titulo = models.CharField(max_length=255, blank=True, null=True)
    paso_confirmacion_contenido = models.TextField(blank=True, null=True)
    paso_confirmacion_texto_boton_final = models.CharField(max_length=255, blank=True, null=True)
    previsualizacion = models.TextField(blank=True, null=True)
    externa = models.IntegerField()
    es_final = models.IntegerField()
    exponer_tramite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea'
        unique_together = (('identificador', 'proceso'),)


class TareaHasGrupoUsuarios(models.Model):
    tarea = models.OneToOneField(Tarea, models.DO_NOTHING, primary_key=True)
    grupo_usuarios = models.ForeignKey(GrupoUsuarios, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarea_has_grupo_usuarios'
        unique_together = (('tarea', 'grupo_usuarios'),)


class Tramite(models.Model):
    proceso = models.ForeignKey(Proceso, models.DO_NOTHING)
    pendiente = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    tramite_proc_cont = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tramite'


class UsersUserprofile(models.Model):
    rut = models.CharField(max_length=200)
    registrado = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20)
    img_perfil = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    usuario = models.OneToOneField(AuthUser, models.DO_NOTHING)
    backend = models.IntegerField()
    frontend = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_userprofile'


class Usuario(models.Model):
    usuario = models.CharField(max_length=128)
    password = models.CharField(max_length=256, blank=True, null=True)
    rut = models.CharField(max_length=16, blank=True, null=True)
    nombres = models.CharField(max_length=128, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=128, blank=True, null=True)
    apellido_materno = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    registrado = models.IntegerField()
    vacaciones = models.IntegerField()
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True, null=True)
    open_id = models.IntegerField()
    reset_token = models.CharField(max_length=40, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_disabled = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('usuario', 'open_id'),)


class UsuarioBackend(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=255)
    nombre = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    rol = models.CharField(max_length=150, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True, null=True)
    reset_token = models.CharField(max_length=40, blank=True, null=True)
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING)
    procesos = models.CharField(max_length=150, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    acepta_terminos = models.IntegerField(blank=True, null=True)
    fecha_aceptacion_terminos = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_disabled = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_backend'
        unique_together = (('cuenta', 'email'),)


class UsuarioManager(models.Model):
    usuario = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=255)
    nombre = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    email = models.TextField(blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_disabled = models.IntegerField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_manager'


class Widget(models.Model):
    tipo = models.CharField(max_length=32)
    nombre = models.CharField(max_length=128)
    posicion = models.PositiveIntegerField()
    config = models.TextField(blank=True, null=True)
    cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'widget'