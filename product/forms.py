from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']

    category = forms.ChoiceField(choices=Product.CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = 'Product Name'

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].label = 'Product Description'

        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].label = 'Product price'

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = 'Product Name'

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].label = 'Product Name'
        