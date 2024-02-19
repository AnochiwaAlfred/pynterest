from django import template


register = template.Library()




@register.simple_tag
def split_uri(uri=""):
    try:
        splitted = str(uri).rsplit("/")
        if len(splitted) > 0:
            formatted = str(splitted[-2])
            return formatted
        return ""
    except Exception as e:
        return str(e)

@register.simple_tag
def get_title(uri="", suffix="", prefix=""):
    try:
        splitted = str(uri).rsplit("/")
        if len(splitted) > 0:
            formatted = str(splitted[-3]) if len(splitted)==4 else str(splitted[-2])
            if prefix!="":
                formatted = prefix + formatted
            if suffix!="":
                formatted += suffix
            print(splitted)
            return formatted
        return ""
    except Exception as e:
        return str(e)
    
