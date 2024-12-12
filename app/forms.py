from django import forms
from .models import Royxat


class RoyxatForm(forms.ModelForm):
    class Meta:
        model = Royxat
        fields = [
            'ism', 'familya', 'viloyat', 'tuman', 'mahhala', 'raqam',
            'kilent', 'aperator', 'sharx', 'status'
        ]
