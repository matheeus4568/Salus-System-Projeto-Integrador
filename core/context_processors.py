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

def breadcrumbs(request):
    if request.path == '/' or request.path.startswith('/admin/'):
        return {'breadcrumbs': []}

    caminho = request.path.strip('/').split('/')
    
    breadcrumbs = []
    url_acumulada = ''

    for parte in caminho:
        url_acumulada += f'/{parte}'
        
        titulo = parte.replace('-', ' ').replace('_', ' ').title()
        
        is_id = parte.isdigit()
        if is_id:
            titulo = f"Detalhes #{parte}"
            

        breadcrumbs.append({
            'title': titulo,
            'url': None if is_id else url_acumulada 
        })
        
    if breadcrumbs:
        breadcrumbs[-1]['url'] = None

    return {'breadcrumbs': breadcrumbs}