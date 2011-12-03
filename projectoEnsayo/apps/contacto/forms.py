from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(max_length = 100)
	mensaje = forms.CharField()
	email	= forms.EmailField()