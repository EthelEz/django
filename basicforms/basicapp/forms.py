from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Nwokem, put your email again!')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self): #This will indicate to django that this is a clean mtd for the entire form.
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        # name = all_cleaned_data['name']
        # text = all_cleaned_data['text']
        vmail = all_cleaned_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure emails match')
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)]) #This page is only going to shown to the html not the user

    # to validate the bot, we use a clean method inside the class form
    # def clean_botcatcher(self): #NB this is a field inside of a class, so we use self
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha Not!")
    #     return botcatcher
