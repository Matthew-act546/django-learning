from typing import Any, Dict
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(
        label="Title", 
        widget=forms.TextInput(
            attrs={
                'placeholder': "Enter a title",
                  }))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Enter description here",
                'class': 'class1 class2',
                'id': 'description-id',
                'rows': 15,
                'cols': 100,
    }))
    email       = forms.EmailField()
    summary     = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Enter description here",
                'class': 'class1 class2',
                'id': 'description-id',
                'rows': 15,
                'cols': 100,
    })
    )
    price       = forms.DecimalField(initial=99.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "MATTHEW" in title:
            raise forms.ValidationError("This is not a title, this is the name of doin this")
        
        return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if email.endswith("edu"):
            raise forms.ValidationError("This is education or deped email")
        return email

class RawProductForm(forms.Form):
    title       = forms.CharField(
        label="Title", 
        widget=forms.TextInput(
            attrs={
                'placeholder': "Enter a title",
                  }))
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Enter description here",
                'class': 'class1 class2',
                'id': 'description-id',
                'rows': 15,
                'cols': 100,
    }))
    price       = forms.DecimalField(initial=99.99)
