from django import template

register = template.Library()

# Map statuses to percentages for the progress bar
STATUS_PROGRESS = {
    'owner': 25,
    'polisher': 50,
    'designer': 75,
    'in_stock': 100,
}

@register.filter(name='status_percentage')
def status_percentage(status):
    return STATUS_PROGRESS.get(status, 0)
