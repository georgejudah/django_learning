from turtle import title
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    # #overiding defaults
    # title = forms.CharField(label= '', widget=forms.TextInput(attrs={'placeholder': 'your-title'}))
    # description = forms.CharField(required=False, widget=forms.Textarea(
    #     attrs={'placeholder': 'your-description',
    #     'class' : 'new-class-name two',
    #     'id': 'description',
    #     'rows':10,
    #     'cols': 50}))
    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'price', 
            'summary'
        ]
    #valdiation for example
    # def clean_title(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a Valid email")
    #     return title
#Pure Django Form
class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    #https://docs.djangoproject.com/en/4.0/ref/forms/fields/