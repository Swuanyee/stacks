from django import forms


class UserUploadForm(forms.Form):
    excelForm = forms.FileField(label='')
