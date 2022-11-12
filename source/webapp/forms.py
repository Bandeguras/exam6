from django import forms
from django.forms import widgets

class BookForm(forms.Form):
    author = forms.CharField(max_length=30, required=True, label='Author')
    email = forms.EmailField(max_length=45, required=True, label='Email')
    description = forms.CharField(max_length=3000, required=True, label='Description', widget=widgets.Textarea(attrs={"cols": 20, "rows": 3}))
