from apps.app.models import Usuario, UsuarioRoles, Permisos, Menu
from functools import wraps
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs
from django.utils.encoding import force_str
from django.utils.six.moves.urllib.parse import urlparse
from django.shortcuts import resolve_url

def iniciar_sesion(request):
	if request.POST["usuario"] == '' or request.POST["password"] == '' :
		return None
	else:
		usuarioCon = None
		nick = request.POST["usuario"]
		clave = request.POST["password"]
		try:
			usuarioCon = Usuario.objects.get(nickUsuario=nick, claveUsuario=clave)
			return usuarioCon.id
		except:
			return None

def cerrar_sesion(request):
    request.session['usuarioSession'] = None

def menu(request):
	menuLista = []
	if request.session.get('usuarioSession') is not None:
		usuarioAux = request.session.get('usuarioSession')	
		listaRoles = UsuarioRoles.objects.filter(usuarioUsurioRoles = usuarioAux)
		if len(listaRoles) > 0:
			listaHabilitada =[]
			listaPermisos = Permisos.objects.all()
			for rolA in listaRoles:
				for per in listaPermisos:
					if rolA == per.rolPermiso:
						listaHabilitada.append(per.menuPermiso.id)
			listaHabilitada = list(set(listaHabilitada))#, id__in=listaHabilitada
			menuLista = Menu.objects.order_by('codigoMenu').filter(estadoMenu='Activo')
	return menuLista;


def usuario_pasa_prueba(test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            # urlparse chokes on lazy objects in Python 3, force to str
            resolved_login_url = force_str(
                resolve_url(login_url or settings.LOGIN_URL))
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                    (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator

def login_requerido(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = usuario_pasa_prueba(
        lambda u: u.is_authenticated(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
