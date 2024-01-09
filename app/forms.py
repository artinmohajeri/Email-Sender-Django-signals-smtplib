from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'id': 'message', 'name':"message", 'rows':'5' , 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':"email",'name':'email','class':'form-control', 'placeholder':'Enter email...', 'maxlength':'254'}))