from django import template

register = template.Library()

@register.filter(name='list_to_natural')
def list_to_natural(value):
    """
    Transforma uma lista de strings em texto de linguagem natural em português.
    Exemplo: ['A', 'B', 'C'] -> 'A, B e C'
    """
    if not isinstance(value, (list, tuple, set)):
        return value
    
    # Converte todos os itens para string e remove espaços vazios
    string_list = [str(item).strip() for item in value if item]
    
    if not string_list:
        return ""
    
    if len(string_list) == 1:
        return string_list[0]
    
    # Junta todos os itens exceto o último com vírgula, e adiciona o último com "e"
    return ", ".join(string_list[:-1]) + " e " + string_list[-1]
