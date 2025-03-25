from django import forms


class Students(forms.Form):
    names = forms.CharField(widget=forms.EmailInput(
        attrs={
            "placeholder": "Enter Your Message...",
            "type": "date",
            "class": 'form-control bg-success-subtle'
        }
    ))

    email = forms.CharField()
    message = forms.CharField()
