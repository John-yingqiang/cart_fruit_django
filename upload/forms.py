from django import forms
 
class UploadForm(forms.Form):
  description = forms.CharField(max_length=50)