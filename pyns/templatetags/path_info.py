from django import template


register = template.Library()




@register.simple_tag
def split_uri1(uri=""):
    try:
        splitted = str(uri).rsplit("/")
        if len(splitted) > 0:
            formatted = str(splitted[-2])
            print(formatted)
            print(formatted)
            return formatted
        return ""
    except Exception as e:
        return str(e)

@register.simple_tag
def split_uri(uri="", suffix="", prefix=""):
    try:
        splitted = str(uri).rsplit("/")
        if len(splitted) > 0:
            formatted = str(splitted[1])
            if prefix!="":
                formatted = prefix + formatted
            if suffix!="":
                formatted += suffix
            return formatted
        return ""
    except Exception as e:
        return str(e)
    
@register.simple_tag
def get_title(uri=""):
    try:
        splitted = str(uri).rsplit("/")
        if len(splitted) > 0:
            formatted = str(splitted[1])
            if formatted!="":
                formatted = "- " + str(splitted[1])
            return formatted
        return ""
    except Exception as e:
        return str(e)