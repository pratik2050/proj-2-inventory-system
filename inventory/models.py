from django.db import models

# Status choices for the monument
STATUS_CHOICES = [
    ('owner', 'Owner'),
    ('polisher', 'Polisher'),
    ('designer', 'Designer'),
    ('in_stock', 'In Stock'),
]

class Monument(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=15, decimal_places=2)  # in grams
    length = models.DecimalField(max_digits=15, decimal_places=2)  # in cm
    width = models.DecimalField(max_digits=15, decimal_places=2)   # in cm
    height = models.DecimalField(max_digits=15, decimal_places=2)  # in cm
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.category})'
