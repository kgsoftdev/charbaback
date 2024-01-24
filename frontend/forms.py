from django import forms
from charbamodel.models import Charba


class CharbaForm(forms.ModelForm):
    class Meta:
        model = Charba
        fields = ['type_charba', 'code', 'code_chars', 'description', 'user']