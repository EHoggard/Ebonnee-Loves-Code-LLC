from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=70)
    email = forms.CharField(max_length=120)
    website = forms.CharField(max_length=200)
    where_from = forms.CharField(max_length=50)
    subjects = (
        ("Web Design & Development", "Web Design & Development"),
        ("Mobile Website", "Mobile Website"),
        ("I Want to General Talk", "I Want to General Talk"),
        ("Other", "Other"),
    )
    subject = forms.ChoiceField(choices = subjects)
    message = forms.CharField(max_length=600)