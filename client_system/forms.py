
from django import forms
from .models import CleintEngament,ClientDetail


class ClientEngagementForm(forms.ModelForm):

    class Meta:
        model=CleintEngament
        fields='__all__'

class ClientDetailForm(forms.ModelForm):

    class Meta:
        model=ClientDetail
        fields='__all__'