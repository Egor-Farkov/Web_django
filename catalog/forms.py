from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

from config.settings import CONSTANT


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["create_at", "updated_at"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя продукта'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['purchase_price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price < 0 :
            raise ValidationError('Цена не должна быть отрицательной')
        return purchase_price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name').strip().lower()
        description = cleaned_data.get('description', '').strip().lower()

        for word in CONSTANT:
            if word in name:
                self.add_error('name', f'Название не может содержать слово {word}')
            if word in description:
                self.add_error('description', f'Описание не может содержать слово {word}')
