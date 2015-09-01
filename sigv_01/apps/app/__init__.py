from apps.app.models import UsuarioRoles, Permisos, Menu, Usuario
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
		return 0
	else:
		usuarioCon = 0
		nick = request.POST["usuario"]
		clave = request.POST["password"]
		try:
			usuarioCon = Usuario.objects.get(nickUsuario=nick, claveUsuario=clave)
			return usuarioCon.id
		except:
			return 0

def cerrar_sesion(request):
    request.session['usuarioSession'] = 5

def menu(request):
    listaHabilitada =[]
    if request.session.get('usuarioSession') is None:
    	print("Okkkkkk")
        request.session["usuarioSession"] = 5
    else:
    	usuarioAux = Usuario.objects.get(id=request.session.get('usuarioSession'))
    	lstUsuRol = UsuarioRoles.objects.filter(usuarioUsuarioRoles = usuarioAux)
    	if len(lstUsuRol) > 0:
        	listaPermisos = Permisos.objects.all().order_by("menuPermiso")
        	for usuRol in lstUsuRol:
        		for per in listaPermisos:
        			if usuRol.rolUsuarioRoles == per.rolPermiso:
        				if per.menuPermiso.urlMenu != "/":
        					url = ""
        				else:
        					url = "/"
        				cont = 0
        				for letra in request.path:
        					if letra == '/':
        						cont = cont + 1
        					if cont ==2:
        						break
        					if letra != '/' and cont < 2:
        						url = url+ letra
        				if url == per.menuPermiso.urlMenu:
        					per.menuPermiso.iconoMenu = "true"
        				if per.menuPermiso.estadoMenu == 'Activo':                            
        					listaHabilitada.append(per.menuPermiso)
			listaAux = []
			for men in listaHabilitada:
				if men in listaAux:
					print("Ya esta")
				else:
					listaAux.append(men)
			return listaAux
	return listaHabilitada

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

def permiso_requerido(request):
    idUsuario = request.session.get("usuarioSession")
    menu = Menu.objects.get(urlMenu=lista_path(request.path))
    lstPermiso = Permisos.objects.filter(menuPermiso=menu)
    if len(lstPermiso)>0:
        return True
    else:
        return False

def lista_path(path):
    path = str(path)

    #if path.find("editar") or path.find("guardar") or path.find(""):
    #    1/0

    diccionarioURL={"/":"/",
    "/quienes_somos/":"quienes_somos",
    "/nuestros_productos/":"nuestros_productos",
    "/contactos/":"contactos",
    "/contable/cuenta_por_cobrar/lista/":"cuentas_por_cobrar",
    "/contable/cuenta_por_pagar/lista/":"cuentas_por_pagar",
    "/general/provincia/lista":"provincias",
    "/general/ciudad/lista":"ciudades",
    "/general/notificacion/lista":"notificaciones",
    "/general/notificacion/nuevo":"nuevo_notificacion",
    "/general/empleado/lista":"empleados",
    "/general/empleado/nuevo":"nuevo_empleado",
    "/general/empleado/editar":"editar_empleado",
    "/general/empleado/eliminar":"eliminar_empleado",
    "/general/empleado/guardar":"guardar_empleado",
    "/general/proveedor/lista":"proveedores",
    "/general/proveedor/nuevo":"nuevo_proveedor",
    "/general/proveedor/editar":"editar_proveedor",
    "/general/proveedor/eliminar":"eliminar_proveedor",
    "/general/proveedor/guardar":"guardar_proveedor",
    "/inventario/producto/lista":"productos",
    "/inventario/producto/nuevo":"nuevo_producto",
    "/inventario/producto/editar":"editar_producto",
    "/inventario/producto/guardar":"guardar_producto",
    "/inventario/producto/eliminar":"eliminar_producto",
    "/inventario/kardex/lista":"kardex",
    "/inventario/categoria/lista":"categorias",
    "/inventario/categoria/nuevo":"nuevo_categoria",
    "/inventario/categoria/editar":"editar_categoria",
    "/inventario/categoria/guardar":"guardar_categoria",
    "/seguridad/usuario/lista":"usuarios",
    "/seguridad/usuario/nuevo":"nuevo_usuario",
    "/seguridad/usuario/editar":"editar_usuario",
    "/seguridad/usuario/eliminar":"eliminar_usuario",
    "/seguridad/usuario/guardar":"guardar_usuario",
    "/seguridad/rol/lista":"roles",
    "/ventas/cliente/lista":"clientes",
    "/ventas/cliente/nuevo":"nuevo_cliente",
    "/ventas/cliente/editar":"editar_cliente",
    "/ventas/cliente/eliminar":"eliminar_cliente",
    "/ventas/cliente/guardar":"guardar_cliente",
    "/ventas/factura/lista":"facturas",
    "/ventas/factura/nuevo":"nuevo_factura",
    "/ventas/factura/editar":"editar_factura",
    "/ventas/factura/eliminar":"eliminar_factura",
    "/ventas/factura/guardar":"guardar_factura",
    }
    return diccionarioURL[path]



def tiene_permiso(request):
    idUsuario = request.session.get("usuarioSession")
    
    """
    Decorator for views that checks whether a user has a particular permission
    enabled, redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
   
    def check_perms(user):
        if not isinstance(perm, (list, tuple)):
            perms = (perm, )
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        if user.has_perms(perms):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return usuario_pasa_prueba(check_perms, login_url=login_url) """
