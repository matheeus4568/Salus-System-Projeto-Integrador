# core/context_processors.py
def sidebar_links(request):
    return {
        "sidebar_links": [
            {"label": "Dashboard", "url_name": "teste", "icon": "icon-monitor", "active_icon": "icon-monitor-marcado"},
            {"label": "Requisições",  "url_name": "teste", "icon": "icon-folders-salus", "active_icon": "icon-folders-salus-marcado"},
            {"label": "Pacientes",   "url_name": "teste", "icon": "icon-pessoas-salus", "active_icon": "icon-pessoas-salus-marcado"},
            {"label": "Secretarias", "url_name": "teste", "icon": "icon-secretaria-salus", "active_icon": "icon-secretaria-salus-marcado"},
            {"label": "Perfil", "url_name": "teste", "icon": "icon-perfil", "active_icon": "icon-perfil-marcado"},
        ]
    }