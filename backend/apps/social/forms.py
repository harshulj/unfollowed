from django import forms

class UserUpdateForm(forms.Form):
    email = forms.EmailField()

