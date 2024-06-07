from django import template 
  
register = template.Library() 
  
@register.filter() 
def get(value, item): 
    return value.get(item)