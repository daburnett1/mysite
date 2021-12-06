from django import forms
from .models import Product

SIZE_CHOICES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('xl', 'XLarge'),
        ('2xl', '2XL'),
        ('3xl', '3XL'),      
)
COLOR_CHOICES = (
    ('black', 'Black'),
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('brown', 'Brown'),
    ('white', 'White'),
)

class pick_size(forms.Form):
    size = forms.CharField(label='Size', widget = forms.Select(choices=SIZE_CHOICES))
    
class pick_color(forms.Form):
    color = forms.CharField(label='Color', widget = forms.Select(choices=COLOR_CHOICES))
    
