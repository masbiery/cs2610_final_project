from django import forms

class SubmitForm(forms.Form):
    message_text = forms.CharField(max_length=1000)