from django import forms
from rn.models import User,UserProfile

class ContactForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        
    
    
class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=40,widget=forms.PasswordInput())
    
