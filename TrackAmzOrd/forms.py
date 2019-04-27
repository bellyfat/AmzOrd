from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    ord_name = forms.CharField(label='label edit',
                widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    
    class Meta:
        model = Order
        fields = [
            'ord_date',
            'ord_url',
            'ord_name'
        ]
