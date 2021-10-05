from django import forms

class TikForm(forms.Form):
    tik_name = forms.CharField(label='', max_length=100)

class TurnoutForm(forms.Form):
    turnout = forms.IntegerField(label='Явка')