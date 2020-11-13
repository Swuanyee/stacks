from django import forms
from django.forms import formset_factory


class DeckForm(forms.Form):
    CHOICES = (
        ("Private", "Private"),
        ('Sec 1', 'Sec 1'),
        ('Sec 2', 'Sec 2'),
        ('Sec 3', 'Sec 3'),
        ('Sec 4', 'Sec 4'),
        ('J1', 'J1'),
        ('J2', 'J2'),
        ('Public', 'Public'),
        ('Teacher', 'Teacher'),
    )

    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'title',
               'placeholder': 'Title'}),
        label='')
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'subject',
               'placeholder': 'Subject'
               }),
        label='')
    availability = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'choices'}),
        label=''
    )


class CardsForm(forms.Form):
    questionText = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'questionText',
               'placeholder': 'Enter your question'
               }),
        label='')
    answerText = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'answerText',
               'placeholder': 'Enter your answer'
               }),
        label='')
    answerImage = forms.ImageField(required=False,
                                   label='',
                                   widget=forms.ClearableFileInput(
                                       attrs={
                                           'class': 'answerImage',
                                       })
                                   )


CardsFormset = formset_factory(CardsForm, extra=250)


class ExcelUploadForm(forms.Form):
    excelForm = forms.FileField(label='')
