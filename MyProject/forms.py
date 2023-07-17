from django import forms

class userForms(forms.Form):
    num_1 = forms.CharField(label="Number 1", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_2 = forms.CharField(label="Number 1", required=True, widget=forms.TextInput())

    email = forms.EmailField(label="Email")

