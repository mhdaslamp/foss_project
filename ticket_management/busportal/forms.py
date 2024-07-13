# busportal/forms.py

from django import forms

class LoginForm(forms.Form):
    adm_no = forms.CharField(label="Admission Number", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
