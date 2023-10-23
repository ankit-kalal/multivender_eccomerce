from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address', 'city', 'state', 'postal_code', 'country']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.required = True
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'shipping_address':
                field.widget.attrs['rows'] = 4  
            