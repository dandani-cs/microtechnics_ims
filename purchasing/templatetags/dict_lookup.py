from django import template

register = template.Library()

@register.filter()
def purchase_item_quantity(item_dict, item_code):
    return item_dict[item_code]
