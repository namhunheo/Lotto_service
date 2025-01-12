from django import forms
from .models import LottoTicket

class LottoForm(forms.ModelForm):
    class Meta:
        model = LottoTicket  # Lotto -> LottoTicket
        fields = ['numbers', 'is_auto']
