from django import template

register = template.Library()

@register.filter()
def purchase_item_quantity(item_dict, item_code):
    return item_dict[item_code]


@register.simple_tag()
def calculate_price_per_item(price_per_unit, quantity):
    return price_per_unit * quantity
