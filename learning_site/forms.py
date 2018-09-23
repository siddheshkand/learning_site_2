from django import forms


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honey = forms.CharField(required=False, widget=forms.HiddenInput)

    # to catch bot
    def clean_honey(self):
        honey = self.cleaned_data['honey']
        if len(honey):
            raise forms.ValidationError(
                "Honey should be blank."
            )
        return honey
