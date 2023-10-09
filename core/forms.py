from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        min_length=5,
        max_length=256,
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )
    subject = forms.CharField(
        max_length=256,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    message = forms.CharField(
        max_length=2048,
        widget=forms.Textarea(attrs={
            'class': 'form-control'
        })
    )
