from django import forms


class UffForm(forms.Form):
    file_field = forms.FileField()

    file_field.widget.attrs.update({'class': 'file'})

