from django import forms
from .models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'


    def clean(self):
        cleaned_data = self.cleaned_data
        qty = cleaned_data.get('qty')
        product = cleaned_data.get('product')
        if qty > product.qty:
            raise forms.ValidationError(u"You have selected more products than are available."
            "There are {0} {1}".format(product.qty, product.title))
        return cleaned_data