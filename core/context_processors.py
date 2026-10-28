# core/context_processors.py
def navbar_links(request):
    return {
        "navbar_links": [
            {"label": "Dashboard", "url_name": "teste", "icon": "icon-monitor", "active_icon": "icon-monitor-solid"},
            {"label": "Requisições",  "url_name": "teste", "icon": "icon-folders", "active_icon": "icon-folders-solid"},
            {"label": "Pacientes",   "url_name": "teste", "icon": "icon-people", "active_icon": "icon-people-solid"},
            {"label": "Secretarias", "url_name": "teste", "icon": "icon-secretary", "active_icon": "icon-secretary-solid"},
            {"label": "Perfil", "url_name": "teste", "icon": "icon-profile", "active_icon": "icon-profile-solid"},
        ]
    }