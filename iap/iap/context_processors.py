def user_app_permissions(request):
    """
    Un procesador de contexto para añadir indicadores de acceso a las aplicaciones
    basándose en la pertenencia a grupos de Django.
    """
    user = request.user
    if not user.is_authenticated:
        return {}

    # Diccionario para los indicadores de acceso, por defecto en falso.
    app_perms = {
        'can_access_cunakids': False,
        'can_access_academia': False,
        'can_access_alabanza': False,
        'can_access_anfitriones': False,
        'can_access_discipulado': False,
        'can_access_encuentros': False,
        'can_access_jap': False,
        'can_access_multimedia': False,
        'can_access_pusukids': False,
    }

    # Los superusuarios siempre tienen acceso a todo.
    if user.is_superuser:
        for key in app_perms:
            app_perms[key] = True
    else:
        # Para usuarios normales, comprobamos si pertenecen a grupos específicos.
        # Asumimos que los grupos se llaman 'cunakids_staff', 'academia_staff', etc.
        if user.groups.filter(name='cunakids_staff').exists():
            app_perms['can_access_cunakids'] = True
        
        # Permiso para Academia (Maestros)
        if user.groups.filter(name='Maestros').exists():
            app_perms['can_access_academia'] = True

        # Permiso para Pusukids
        if user.groups.filter(name='pusukids_staff').exists():
            app_perms['can_access_pusukids'] = True

    return {'app_perms': app_perms}