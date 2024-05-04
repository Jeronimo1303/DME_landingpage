from django import forms

class new_search(forms.Form):
    search = forms.CharField(label = "Search", max_length=200)