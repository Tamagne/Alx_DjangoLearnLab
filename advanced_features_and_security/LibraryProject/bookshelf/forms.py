# bookshelf/forms.py

from django import forms

class ExampleForm(forms.Form):
    """
    A simple example form for demonstration purposes.
    """
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'form-control'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Write your message here',
        'rows': 4,
        'class': 'form-control'
    }))
