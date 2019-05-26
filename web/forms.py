from django import forms


class DocumentUploadForm(forms.Form):

    data = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': '6',
                'placeholder': 'paste your json formatted data here',
                'class': 'form-control',
            }),
        required=True,
    )
